from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from models import Event, Base
from schemas import Event as EventSchema, EventCreate
from database import engine, get_db

Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/eventos", response_model=List[EventSchema])
def read_events(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    events = db.query(Event).offset(skip).limit(limit).all()
    return events

@router.get("/eventos/{id}", response_model=EventSchema)
def read_event(id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == id).first()
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.post("/eventos", response_model=EventSchema)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    db_event = Event(nome=event.nome, descricao=event.descricao)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event