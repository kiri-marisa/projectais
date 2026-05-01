from datetime import date, time, datetime
from pydantic import BaseModel, ConfigDict
from typing import Optional


class RoleBase(BaseModel):
    name: str


class RoleOut(RoleBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class UserBase(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    email: str
    role_id: int
    is_active: bool = True


class UserCreate(UserBase):
    password_hash: str


class UserUpdateEmail(BaseModel):
    email: str


class UserOut(UserBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class RoomBase(BaseModel):
    name: str
    capacity: int


class RoomCreate(RoomBase):
    pass


class RoomOut(RoomBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class TrainingBase(BaseModel):
    title: str
    description: Optional[str] = None
    training_date: date
    start_time: time
    end_time: time
    trainer_id: int
    room_id: int
    max_participants: int
    status: str = "planned"


class TrainingCreate(TrainingBase):
    pass


class TrainingOut(TrainingBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class BookingBase(BaseModel):
    user_id: int
    training_id: int
    status: str = "booked"


class BookingCreate(BookingBase):
    pass


class BookingOut(BookingBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class SubscriptionBase(BaseModel):
    title: str
    price: int
    duration_days: int
    training_count: int
    description: Optional[str] = None


class SubscriptionCreate(SubscriptionBase):
    pass


class SubscriptionOut(SubscriptionBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class MembershipBase(BaseModel):
    user_id: int
    subscription_id: int
    start_date: date
    end_date: date
    remaining_trainings: int
    status: str = "active"


class MembershipCreate(MembershipBase):
    pass


class MembershipOut(MembershipBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class SubRequestBase(BaseModel):
    user_id: int
    subscription_id: int
    status: str = "pending"


class SubRequestCreate(SubRequestBase):
    pass


class SubRequestUpdateStatus(BaseModel):
    status: str


class SubRequestOut(SubRequestBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)