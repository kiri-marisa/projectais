import random
from datetime import date, timedelta, time

from sqlalchemy import text

from database import SessionLocal
from models import Role, User, Room, Training, Subscription


def clear_data(db):
    print("Очистка старых данных...")

    db.execute(text("DELETE FROM bookings"))
    db.execute(text("DELETE FROM memberships"))
    db.execute(text("DELETE FROM sub_requests"))
    db.execute(text("DELETE FROM trainings"))
    db.execute(text("DELETE FROM rooms"))
    db.execute(text("DELETE FROM users WHERE id > 3"))
    db.execute(text("DELETE FROM subscriptions WHERE id > 2"))

    db.commit()


def seed_roles(db):
    if not db.query(Role).first():
        db.add_all([
            Role(name="admin"),
            Role(name="trainer"),
            Role(name="client")
        ])
        db.commit()


def seed_users(db):
    print("Создание пользователей...")

    trainer_role = db.query(Role).filter_by(name="trainer").first()
    client_role = db.query(Role).filter_by(name="client").first()

    for i in range(5):
        db.add(User(
            first_name=f"Trainer{i}",
            last_name="Test",
            phone_number=f"+79990000{i+100}",
            email=f"trainer{i}@test.com",
            password_hash="123",
            role_id=trainer_role.id,
            is_active=True
        ))

    for i in range(50):
        db.add(User(
            first_name=f"Client{i}",
            last_name="Test",
            phone_number=f"+7999111{i+100}",
            email=f"client{i}@test.com",
            password_hash="123",
            role_id=client_role.id,
            is_active=True
        ))

    db.commit()


def seed_rooms(db):
    print("Создание залов...")

    for i in range(5):
        db.add(Room(
            name=f"Зал {i+1}",
            capacity=random.randint(10, 30)
        ))

    db.commit()


def seed_subscriptions(db):
    print("Создание абонементов...")

    for i in range(5):
        db.add(Subscription(
            title=f"Абонемент {i}",
            price=random.randint(2000, 6000),
            duration_days=30,
            training_count=random.randint(5, 20),
            description="Auto generated"
        ))

    db.commit()


def seed_trainings(db):
    print("Создание тренировок...")

    trainers = db.query(User).filter(User.role_id == 2).all()
    rooms = db.query(Room).all()

    for i in range(20):
        trainer = random.choice(trainers)
        room = random.choice(rooms)
        start_hour = random.randint(8, 18)

        db.add(Training(
            title=f"Тренировка {i}",
            description="Auto generated",
            training_date=date.today() + timedelta(days=random.randint(1, 10)),
            start_time=time(start_hour, 0),
            end_time=time(start_hour + 1, 0),
            trainer_id=trainer.id,
            room_id=room.id,
            max_participants=random.randint(5, room.capacity),
            status="planned"
        ))

    db.commit()


def seed_data():
    db = SessionLocal()

    try:
        seed_roles(db)
        clear_data(db)
        seed_users(db)
        seed_rooms(db)
        seed_subscriptions(db)
        seed_trainings(db)

        print("Данные успешно сгенерированы!")

    finally:
        db.close()


if __name__ == "__main__":
    seed_data()