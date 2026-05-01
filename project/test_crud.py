import unittest
from datetime import date, time, timedelta

from database import SessionLocal
from models import Role, User, Room, Training, Booking, Subscription, Membership, SubRequest
from crud import (
    create_user,
    get_users,
    get_user_by_id,
    update_user_email,
    delete_user,
    create_room,
    get_rooms,
    create_training,
    get_trainings,
    create_booking,
    get_bookings,
    cancel_booking,
    create_subscription,
    get_subscriptions,
    create_sub_request,
    get_sub_requests,
    update_sub_request_status,
)


class TestCRUD(unittest.TestCase):

    def setUp(self):
        self.db = SessionLocal()

        # роли должны уже быть после seed.py
        self.admin_role = self.db.query(Role).filter_by(name="admin").first()
        self.trainer_role = self.db.query(Role).filter_by(name="trainer").first()
        self.client_role = self.db.query(Role).filter_by(name="client").first()

        self.assertIsNotNone(self.admin_role)
        self.assertIsNotNone(self.trainer_role)
        self.assertIsNotNone(self.client_role)

    def tearDown(self):
        self.db.close()

    # ---------------- USERS ----------------

    def test_01_create_user(self):
        user = create_user(
            db=self.db,
            first_name="Тест",
            last_name="Пользователь",
            phone_number="+79991112233",
            email="testuser1@gymcrm.local",
            password_hash="test123",
            role_id=self.client_role.id,
            is_active=True
        )
        self.assertIsNotNone(user.id)
        self.assertEqual(user.email, "testuser1@gymcrm.local")

    def test_02_get_users(self):
        users = get_users(self.db)
        self.assertIsInstance(users, list)
        self.assertGreaterEqual(len(users), 1)

    def test_03_update_user_email(self):
        user = create_user(
            db=self.db,
            first_name="Иван",
            last_name="Смирнов",
            phone_number="+79991112234",
            email="oldmail@gymcrm.local",
            password_hash="123",
            role_id=self.client_role.id,
            is_active=True
        )

        updated_user = update_user_email(self.db, user.id, "newmail@gymcrm.local")
        self.assertEqual(updated_user.email, "newmail@gymcrm.local")

    def test_04_delete_user(self):
        user = create_user(
            db=self.db,
            first_name="Удаляемый",
            last_name="Пользователь",
            phone_number="+79991112235",
            email="deleteuser@gymcrm.local",
            password_hash="123",
            role_id=self.client_role.id,
            is_active=True
        )

        delete_user(self.db, user.id)
        deleted = get_user_by_id(self.db, user.id)
        self.assertIsNone(deleted)

    # ---------------- ROOMS ----------------

    def test_05_create_room(self):
        room = create_room(self.db, "Тестовый зал", 12)
        self.assertIsNotNone(room.id)
        self.assertEqual(room.name, "Тестовый зал")

    def test_06_get_rooms(self):
        rooms = get_rooms(self.db)
        self.assertIsInstance(rooms, list)
        self.assertGreaterEqual(len(rooms), 1)

    # ---------------- TRAININGS ----------------

    def test_07_create_training(self):
        trainer = create_user(
            db=self.db,
            first_name="Тренер",
            last_name="Тестов",
            phone_number="+79991112236",
            email="trainer_test1@gymcrm.local",
            password_hash="123",
            role_id=self.trainer_role.id,
            is_active=True
        )

        room = create_room(self.db, "Зал для тренировки", 20)

        training = create_training(
            db=self.db,
            title="Йога",
            description="Тестовая тренировка",
            training_date=date.today() + timedelta(days=3),
            start_time=time(9, 0),
            end_time=time(10, 0),
            trainer_id=trainer.id,
            room_id=room.id,
            max_participants=10,
            status="planned"
        )

        self.assertIsNotNone(training.id)
        self.assertEqual(training.title, "Йога")

    def test_08_get_trainings(self):
        trainings = get_trainings(self.db)
        self.assertIsInstance(trainings, list)
        self.assertGreaterEqual(len(trainings), 1)

    # ---------------- BOOKINGS ----------------

    def test_09_create_booking(self):
        client = create_user(
            db=self.db,
            first_name="Клиент",
            last_name="Бронирования",
            phone_number="+79991112237",
            email="client_booking1@gymcrm.local",
            password_hash="123",
            role_id=self.client_role.id,
            is_active=True
        )

        trainer = create_user(
            db=self.db,
            first_name="Тренер",
            last_name="Бронирования",
            phone_number="+79991112238",
            email="trainer_booking1@gymcrm.local",
            password_hash="123",
            role_id=self.trainer_role.id,
            is_active=True
        )

        room = create_room(self.db, "Зал бронирования", 15)

        training = create_training(
            db=self.db,
            title="Пилатес",
            description="Тренировка для бронирования",
            training_date=date.today() + timedelta(days=5),
            start_time=time(12, 0),
            end_time=time(13, 0),
            trainer_id=trainer.id,
            room_id=room.id,
            max_participants=5,
            status="planned"
        )

        booking = create_booking(self.db, client.id, training.id)
        self.assertIsNotNone(booking.id)
        self.assertEqual(booking.status, "booked")

    def test_10_create_duplicate_booking_should_fail(self):
        client = create_user(
            db=self.db,
            first_name="Клиент",
            last_name="Дубль",
            phone_number="+79991112239",
            email="client_duplicate@gymcrm.local",
            password_hash="123",
            role_id=self.client_role.id,
            is_active=True
        )

        trainer = create_user(
            db=self.db,
            first_name="Тренер",
            last_name="Дубль",
            phone_number="+79991112240",
            email="trainer_duplicate@gymcrm.local",
            password_hash="123",
            role_id=self.trainer_role.id,
            is_active=True
        )

        room = create_room(self.db, "Зал дублей", 10)

        training = create_training(
            db=self.db,
            title="Кроссфит",
            description="Проверка дубля записи",
            training_date=date.today() + timedelta(days=4),
            start_time=time(14, 0),
            end_time=time(15, 0),
            trainer_id=trainer.id,
            room_id=room.id,
            max_participants=5,
            status="planned"
        )

        create_booking(self.db, client.id, training.id)

        with self.assertRaises(ValueError):
            create_booking(self.db, client.id, training.id)

    def test_11_cancel_booking(self):
        client = create_user(
            db=self.db,
            first_name="Клиент",
            last_name="Отмена",
            phone_number="+79991112241",
            email="client_cancel@gymcrm.local",
            password_hash="123",
            role_id=self.client_role.id,
            is_active=True
        )

        trainer = create_user(
            db=self.db,
            first_name="Тренер",
            last_name="Отмена",
            phone_number="+79991112242",
            email="trainer_cancel@gymcrm.local",
            password_hash="123",
            role_id=self.trainer_role.id,
            is_active=True
        )

        room = create_room(self.db, "Зал отмены", 8)

        training = create_training(
            db=self.db,
            title="Стретчинг",
            description="Проверка отмены записи",
            training_date=date.today() + timedelta(days=6),
            start_time=time(16, 0),
            end_time=time(17, 0),
            trainer_id=trainer.id,
            room_id=room.id,
            max_participants=5,
            status="planned"
        )

        booking = create_booking(self.db, client.id, training.id)
        cancelled = cancel_booking(self.db, booking.id)

        self.assertEqual(cancelled.status, "cancelled")

    def test_12_get_bookings(self):
        bookings = get_bookings(self.db)
        self.assertIsInstance(bookings, list)

    # ---------------- SUBSCRIPTIONS ----------------

    def test_13_create_subscription(self):
        subscription = create_subscription(
            db=self.db,
            title="Тестовый абонемент",
            price=2500,
            duration_days=30,
            training_count=6,
            description="Абонемент для теста"
        )

        self.assertIsNotNone(subscription.id)
        self.assertEqual(subscription.title, "Тестовый абонемент")

    def test_14_get_subscriptions(self):
        subscriptions = get_subscriptions(self.db)
        self.assertIsInstance(subscriptions, list)
        self.assertGreaterEqual(len(subscriptions), 1)

    # ---------------- SUB REQUESTS ----------------

    def test_15_create_sub_request(self):
        client = create_user(
            db=self.db,
            first_name="Клиент",
            last_name="Заявка",
            phone_number="+79991112243",
            email="client_request@gymcrm.local",
            password_hash="123",
            role_id=self.client_role.id,
            is_active=True
        )

        subscription = create_subscription(
            db=self.db,
            title="Абонемент для заявки",
            price=3500,
            duration_days=30,
            training_count=10,
            description="Проверка заявки"
        )

        sub_request = create_sub_request(self.db, client.id, subscription.id)
        self.assertIsNotNone(sub_request.id)
        self.assertEqual(sub_request.status, "pending")

    def test_16_update_sub_request_status(self):
        client = create_user(
            db=self.db,
            first_name="Клиент",
            last_name="Одобрение",
            phone_number="+79991112244",
            email="client_approve@gymcrm.local",
            password_hash="123",
            role_id=self.client_role.id,
            is_active=True
        )

        subscription = create_subscription(
            db=self.db,
            title="Абонемент на одобрение",
            price=4000,
            duration_days=60,
            training_count=12,
            description="Проверка смены статуса"
        )

        sub_request = create_sub_request(self.db, client.id, subscription.id)
        updated_request = update_sub_request_status(self.db, sub_request.id, "approved")

        self.assertEqual(updated_request.status, "approved")

    def test_17_get_sub_requests(self):
        sub_requests = get_sub_requests(self.db)
        self.assertIsInstance(sub_requests, list)


if __name__ == "__main__":
    unittest.main()