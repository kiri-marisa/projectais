from sqlalchemy import (
    Column, Integer, String, ForeignKey, Date, Time,
    Boolean, DateTime, Text, UniqueConstraint
)
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    users = relationship("User", back_populates="role")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone_number = Column(String(20), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    role = relationship("Role", back_populates="users")
    trainings = relationship("Training", back_populates="trainer")
    bookings = relationship("Booking", back_populates="user")
    memberships = relationship("Membership", back_populates="user")
    subscription_requests = relationship("SubRequest", back_populates="user")


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    capacity = Column(Integer, nullable=False)

    trainings = relationship("Training", back_populates="room")


class Training(Base):
    __tablename__ = "trainings"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    training_date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    trainer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.id"), nullable=False)
    max_participants = Column(Integer, nullable=False)
    status = Column(String(20), default="planned")
    created_at = Column(DateTime, default=datetime.utcnow)

    trainer = relationship("User", back_populates="trainings")
    room = relationship("Room", back_populates="trainings")
    bookings = relationship("Booking", back_populates="training", cascade="all, delete-orphan")


class Booking(Base):
    __tablename__ = "bookings"
    __table_args__ = (
        UniqueConstraint("user_id", "training_id", name="uq_user_training"),
    )

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    training_id = Column(Integer, ForeignKey("trainings.id"), nullable=False)
    status = Column(String(20), default="booked")
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="bookings")
    training = relationship("Training", back_populates="bookings")


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    price = Column(Integer, nullable=False)
    duration_days = Column(Integer, nullable=False)
    training_count = Column(Integer, nullable=False)
    description = Column(Text)

    memberships = relationship("Membership", back_populates="subscription")
    requests = relationship("SubRequest", back_populates="subscription")


class Membership(Base):
    __tablename__ = "memberships"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    subscription_id = Column(Integer, ForeignKey("subscriptions.id"), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    remaining_trainings = Column(Integer, nullable=False)
    status = Column(String(20), default="active")

    user = relationship("User", back_populates="memberships")
    subscription = relationship("Subscription", back_populates="memberships")


class SubRequest(Base):
    __tablename__ = "sub_requests"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    subscription_id = Column(Integer, ForeignKey("subscriptions.id"), nullable=False)
    status = Column(String(20), default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="subscription_requests")
    subscription = relationship("Subscription", back_populates="requests")