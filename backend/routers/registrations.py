from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models import Registration, Event, User, Base
from schemas import RegistrationCreate, Registration as RegistrationSchema
from database import engine, get_db

Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.post("/inscricoes", response_model=RegistrationSchema)
def create_registration(registration: RegistrationCreate, db: Session = Depends(get_db)):
    db_event = db.query(Event).filter(Event.id == registration.event_id).first()
    db_user = db.query(User).filter(User.id == registration.user_id).first()
    if not db_event or not db_user:
        raise HTTPException(status_code=404, detail="Event or User not found")
    db_registration = Registration(event_id=registration.event_id, user_id=registration.user_id)
    db.add(db_registration)
    db.commit()
    db.refresh(db_registration)
    return db_registration

@router.get("/inscricoes/{user_id}", response_model=List[RegistrationSchema])
def read_registrations(user_id: int, db: Session = Depends(get_db)):
    registrations = db.query(Registration).filter(Registration.user_id == user_id).all()
    return registrations

@router.delete("/inscricoes/{registration_id}", response_model=RegistrationSchema)
def delete_registration(registration_id: int, db: Session = Depends(get_db)):
    db_registration = db.query(Registration).filter(Registration.id == registration_id).first()
    if db_registration is None:
        raise HTTPException(status_code=404, detail="Registration not found")
    db.delete(db_registration)
    db.commit()
    return db_registration