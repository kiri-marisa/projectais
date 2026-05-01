from sqlalchemy.orm import Session
from models import User, Role, Room, Training, Booking, Subscription, Membership, SubRequest


# ---------------- USERS ----------------

def create_user(
    db: Session,
    first_name: str,
    last_name: str,
    phone_number: str,
    email: str,
    password_hash: str,
    role_id: int,
    is_active: bool = True
):
    user = User(
        first_name=first_name,
        last_name=last_name,
        phone_number=phone_number,
        email=email,
        password_hash=password_hash,
        role_id=role_id,
        is_active=is_active
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def update_user_email(db: Session, user_id: int, new_email: str):
    user = get_user_by_id(db, user_id)
    if user:
        user.email = new_email
        db.commit()
        db.refresh(user)
    return user


def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if user:
        db.delete(user)
        db.commit()
    return user


# ---------------- ROLES ----------------

def get_roles(db: Session):
    return db.query(Role).all()


# ---------------- ROOMS ----------------

def create_room(db: Session, name: str, capacity: int):
    room = Room(name=name, capacity=capacity)
    db.add(room)
    db.commit()
    db.refresh(room)
    return room


def get_rooms(db: Session):
    return db.query(Room).all()


# ---------------- TRAININGS ----------------

def create_training(
    db: Session,
    title: str,
    description: str,
    training_date,
    start_time,
    end_time,
    trainer_id: int,
    room_id: int,
    max_participants: int,
    status: str = "planned"
):
    training = Training(
        title=title,
        description=description,
        training_date=training_date,
        start_time=start_time,
        end_time=end_time,
        trainer_id=trainer_id,
        room_id=room_id,
        max_participants=max_participants,
        status=status
    )
    db.add(training)
    db.commit()
    db.refresh(training)
    return training


def get_trainings(db: Session):
    return db.query(Training).all()


def get_training_by_id(db: Session, training_id: int):
    return db.query(Training).filter(Training.id == training_id).first()


def update_training_status(db: Session, training_id: int, new_status: str):
    training = get_training_by_id(db, training_id)
    if training:
        training.status = new_status
        db.commit()
        db.refresh(training)
    return training


def delete_training(db: Session, training_id: int):
    training = get_training_by_id(db, training_id)
    if training:
        db.delete(training)
        db.commit()
    return training


# ---------------- BOOKINGS ----------------

def create_booking(db: Session, user_id: int, training_id: int, status: str = "booked"):
    # Проверка: пользователь существует
    user = get_user_by_id(db, user_id)
    if not user:
        raise ValueError("Пользователь не найден")

    # Проверка: тренировка существует
    training = get_training_by_id(db, training_id)
    if not training:
        raise ValueError("Тренировка не найдена")

    # Проверка: нельзя записаться на отмененную тренировку
    if training.status == "cancelled":
        raise ValueError("Нельзя записаться на отменённую тренировку")

    # Проверка: нет ли уже записи
    existing_booking = db.query(Booking).filter(
        Booking.user_id == user_id,
        Booking.training_id == training_id
    ).first()

    if existing_booking:
        raise ValueError("Пользователь уже записан на эту тренировку")

    # Проверка: есть ли свободные места
    active_bookings_count = db.query(Booking).filter(
        Booking.training_id == training_id,
        Booking.status == "booked"
    ).count()

    if active_bookings_count >= training.max_participants:
        raise ValueError("Свободных мест нет")

    booking = Booking(
        user_id=user_id,
        training_id=training_id,
        status=status
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking


def get_bookings(db: Session):
    return db.query(Booking).all()


def cancel_booking(db: Session, booking_id: int):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if booking:
        booking.status = "cancelled"
        db.commit()
        db.refresh(booking)
    return booking


# ---------------- SUBSCRIPTIONS ----------------

def create_subscription(
    db: Session,
    title: str,
    price: int,
    duration_days: int,
    training_count: int,
    description: str = None
):
    subscription = Subscription(
        title=title,
        price=price,
        duration_days=duration_days,
        training_count=training_count,
        description=description
    )
    db.add(subscription)
    db.commit()
    db.refresh(subscription)
    return subscription


def get_subscriptions(db: Session):
    return db.query(Subscription).all()


# ---------------- MEMBERSHIPS ----------------

def create_membership(
    db: Session,
    user_id: int,
    subscription_id: int,
    start_date,
    end_date,
    remaining_trainings: int,
    status: str = "active"
):
    membership = Membership(
        user_id=user_id,
        subscription_id=subscription_id,
        start_date=start_date,
        end_date=end_date,
        remaining_trainings=remaining_trainings,
        status=status
    )
    db.add(membership)
    db.commit()
    db.refresh(membership)
    return membership


def get_memberships(db: Session):
    return db.query(Membership).all()


# ---------------- SUB REQUESTS ----------------

def create_sub_request(db: Session, user_id: int, subscription_id: int, status: str = "pending"):
    sub_request = SubRequest(
        user_id=user_id,
        subscription_id=subscription_id,
        status=status
    )
    db.add(sub_request)
    db.commit()
    db.refresh(sub_request)
    return sub_request


def get_sub_requests(db: Session):
    return db.query(SubRequest).all()


def update_sub_request_status(db: Session, request_id: int, new_status: str):
    sub_request = db.query(SubRequest).filter(SubRequest.id == request_id).first()
    if sub_request:
        sub_request.status = new_status
        db.commit()
        db.refresh(sub_request)
    return sub_request