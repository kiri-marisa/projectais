from locust import HttpUser, task, between, tag
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import random


# Windows -> SSH tunnel -> MariaDB on VM
DATABASE_URL = "mysql+mysqlconnector://gym_user:1234@127.0.0.1:3307/gym_crm"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def load_ids(query: str):
    db = SessionLocal()
    try:
        rows = db.execute(text(query)).fetchall()
        return [row[0] for row in rows]
    finally:
        db.close()


USER_IDS = load_ids("SELECT id FROM users")
TRAINING_IDS = load_ids("SELECT id FROM trainings")
SUBSCRIPTION_IDS = load_ids("SELECT id FROM subscriptions")


class GymCRMUser(HttpUser):
    wait_time = between(0.5, 1.5)

    @tag("get_put", "with_post")
    @task(4)
    def get_users(self):
        self.client.get("/users", name="GET /users")

    @tag("get_put", "with_post")
    @task(5)
    def get_trainings(self):
        self.client.get("/trainings", name="GET /trainings")

    @tag("get_put", "with_post")
    @task(3)
    def get_subscriptions(self):
        self.client.get("/subscriptions", name="GET /subscriptions")

    @tag("get_put", "with_post")
    @task(2)
    def update_user_email(self):
        if not USER_IDS:
            return

        user_id = random.choice(USER_IDS)
        payload = {
            "email": f"loadtest{random.randint(1, 1000000)}@test.com"
        }

        with self.client.put(
            f"/users/{user_id}/email",
            json=payload,
            name="PUT /users/{id}/email",
            catch_response=True
        ) as response:
            if response.status_code in (200, 404):
                response.success()
            else:
                response.failure(f"Unexpected status: {response.status_code}")

    @tag("with_post")
    @task(2)
    def create_booking(self):
        if not USER_IDS or not TRAINING_IDS:
            return

        payload = {
            "user_id": random.choice(USER_IDS),
            "training_id": random.choice(TRAINING_IDS),
            "status": "booked"
        }

        with self.client.post(
            "/bookings",
            json=payload,
            name="POST /bookings",
            catch_response=True
        ) as response:
            if response.status_code in (200, 400):
                # 400 здесь допустимы: дубль записи, нет мест и т.п.
                response.success()
            else:
                response.failure(f"Unexpected status: {response.status_code}")

    @tag("with_post")
    @task(2)
    def create_sub_request(self):
        if not USER_IDS or not SUBSCRIPTION_IDS:
            return

        payload = {
            "user_id": random.choice(USER_IDS),
            "subscription_id": random.choice(SUBSCRIPTION_IDS),
            "status": "pending"
        }

        with self.client.post(
            "/sub-requests",
            json=payload,
            name="POST /sub-requests",
            catch_response=True
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Unexpected status: {response.status_code}")