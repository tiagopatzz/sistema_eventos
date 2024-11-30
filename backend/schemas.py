from pydantic import BaseModel
from typing import List

class UserCreate(BaseModel):
    nome: str
    email: str
    senha: str

class User(BaseModel):
    id: int
    nome: str
    email: str

    class Config:
        from_attributes = True

class EventCreate(BaseModel):
    nome: str
    descricao: str

class Event(BaseModel):
    id: int
    nome: str
    descricao: str

    class Config:
        from_attributes = True

class RegistrationCreate(BaseModel):
    event_id: int
    user_id: int

class Registration(BaseModel):
    id: int
    event_id: int
    user_id: int

    class Config:
        from_attributes = True