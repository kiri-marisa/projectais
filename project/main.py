from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
import crud
import schemas

app = FastAPI(title="Gym CRM API")


# ---------------- DB SESSION ----------------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- ROOT ----------------

@app.get("/")
def root():
    return {"message": "Gym CRM API is running"}


# ---------------- USERS ----------------

@app.get("/users", response_model=list[schemas.UserOut])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


@app.post("/users", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = crud.get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email already exists")

    return crud.create_user(
        db=db,
        first_name=user.first_name,
        last_name=user.last_name,
        phone_number=user.phone_number,
        email=user.email,
        password_hash=user.password_hash,
        role_id=user.role_id,
        is_active=user.is_active
    )


@app.get("/users/{user_id}", response_model=schemas.UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.put("/users/{user_id}/email", response_model=schemas.UserOut)
def update_user_email(user_id: int, payload: schemas.UserUpdateEmail, db: Session = Depends(get_db)):
    user = crud.update_user_email(db, user_id, payload.email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}


# ---------------- ROLES ----------------

@app.get("/roles", response_model=list[schemas.RoleOut])
def read_roles(db: Session = Depends(get_db)):
    return crud.get_roles(db)


# ---------------- ROOMS ----------------

@app.get("/rooms", response_model=list[schemas.RoomOut])
def read_rooms(db: Session = Depends(get_db)):
    return crud.get_rooms(db)


@app.post("/rooms", response_model=schemas.RoomOut)
def create_room(room: schemas.RoomCreate, db: Session = Depends(get_db)):
    return crud.create_room(db, room.name, room.capacity)


# ---------------- TRAININGS ----------------

@app.get("/trainings", response_model=list[schemas.TrainingOut])
def read_trainings(db: Session = Depends(get_db)):
    return crud.get_trainings(db)


@app.get("/trainings/{training_id}", response_model=schemas.TrainingOut)
def read_training(training_id: int, db: Session = Depends(get_db)):
    training = crud.get_training_by_id(db, training_id)
    if not training:
        raise HTTPException(status_code=404, detail="Training not found")
    return training


@app.post("/trainings", response_model=schemas.TrainingOut)
def create_training(training: schemas.TrainingCreate, db: Session = Depends(get_db)):
    return crud.create_training(
        db=db,
        title=training.title,
        description=training.description,
        training_date=training.training_date,
        start_time=training.start_time,
        end_time=training.end_time,
        trainer_id=training.trainer_id,
        room_id=training.room_id,
        max_participants=training.max_participants,
        status=training.status
    )


# ---------------- BOOKINGS ----------------

@app.get("/bookings", response_model=list[schemas.BookingOut])
def read_bookings(db: Session = Depends(get_db)):
    return crud.get_bookings(db)


@app.post("/bookings", response_model=schemas.BookingOut)
def create_booking(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_booking(
            db=db,
            user_id=booking.user_id,
            training_id=booking.training_id,
            status=booking.status
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.put("/bookings/{booking_id}/cancel", response_model=schemas.BookingOut)
def cancel_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = crud.cancel_booking(db, booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking


# ---------------- SUBSCRIPTIONS ----------------

@app.get("/subscriptions", response_model=list[schemas.SubscriptionOut])
def read_subscriptions(db: Session = Depends(get_db)):
    return crud.get_subscriptions(db)


@app.post("/subscriptions", response_model=schemas.SubscriptionOut)
def create_subscription(subscription: schemas.SubscriptionCreate, db: Session = Depends(get_db)):
    return crud.create_subscription(
        db=db,
        title=subscription.title,
        price=subscription.price,
        duration_days=subscription.duration_days,
        training_count=subscription.training_count,
        description=subscription.description
    )


# ---------------- MEMBERSHIPS ----------------

@app.get("/memberships", response_model=list[schemas.MembershipOut])
def read_memberships(db: Session = Depends(get_db)):
    return crud.get_memberships(db)


@app.post("/memberships", response_model=schemas.MembershipOut)
def create_membership(membership: schemas.MembershipCreate, db: Session = Depends(get_db)):
    return crud.create_membership(
        db=db,
        user_id=membership.user_id,
        subscription_id=membership.subscription_id,
        start_date=membership.start_date,
        end_date=membership.end_date,
        remaining_trainings=membership.remaining_trainings,
        status=membership.status
    )


# ---------------- SUB REQUESTS ----------------

@app.get("/sub-requests", response_model=list[schemas.SubRequestOut])
def read_sub_requests(db: Session = Depends(get_db)):
    return crud.get_sub_requests(db)


@app.post("/sub-requests", response_model=schemas.SubRequestOut)
def create_sub_request(sub_request: schemas.SubRequestCreate, db: Session = Depends(get_db)):
    return crud.create_sub_request(
        db=db,
        user_id=sub_request.user_id,
        subscription_id=sub_request.subscription_id,
        status=sub_request.status
    )


@app.put("/sub-requests/{request_id}/status", response_model=schemas.SubRequestOut)
def update_sub_request_status(
    request_id: int,
    payload: schemas.SubRequestUpdateStatus,
    db: Session = Depends(get_db)
):
    sub_request = crud.update_sub_request_status(db, request_id, payload.status)
    if not sub_request:
        raise HTTPException(status_code=404, detail="Subscription request not found")
    return sub_request