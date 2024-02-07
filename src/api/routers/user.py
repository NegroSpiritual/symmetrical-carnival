from fastapi import APIRouter, HTTPException, Depends
from db.db import engine, SessionLocal, Base
from sqlalchemy.orm import Session
from typing_extensions import Annotated


router = APIRouter(
    tags = ['USER'],
    prefix = '/user'
)
Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]