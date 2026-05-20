from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db import models
from app.schemas import wallet as schema

router = APIRouter()

@router.get("/{employee_id}", response_model=schema.WalletInfo)
def get_wallet(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return schema.WalletInfo(balance=employee.monthly_balance, daily_limit=employee.daily_limit)
