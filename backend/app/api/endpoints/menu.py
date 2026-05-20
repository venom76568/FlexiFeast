from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.db import models
from app.schemas import menu as menu_schema

router = APIRouter()

@router.get("/", response_model=List[menu_schema.MenuItem])
def get_menu_items(db: Session = Depends(get_db)):
    items = db.query(models.CanteenMenu).all()
    return items

@router.post("/", response_model=menu_schema.MenuItem)
def create_menu_item(item: menu_schema.MenuItemCreate, db: Session = Depends(get_db)):
    db_item = models.CanteenMenu(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
