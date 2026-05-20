from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.db import models
from app.schemas import transactions as schema
from app.services.split_pay import calculate_split_payment

router = APIRouter()

@router.post("/", response_model=schema.TransactionResponse)
def create_transaction(transaction: schema.TransactionCreate, db: Session = Depends(get_db)):
    # SECURITY: Verify split payment logic on backend (A06: Insecure Design)
    employee = db.query(models.Employee).filter(models.Employee.id == transaction.employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
        
    expected_split = calculate_split_payment(transaction.total_cart_amount, employee.daily_limit)
    if abs(expected_split["wallet_deducted"] - transaction.wallet_deducted_amount) > 0.01 or \
       abs(expected_split["personal_paid"] - transaction.personal_paid_amount) > 0.01:
        raise HTTPException(status_code=400, detail="Invalid payment split payload. Potential manipulation detected.")

    # Deduct from monthly balance
    if expected_split["wallet_deducted"] > employee.monthly_balance:
        raise HTTPException(status_code=400, detail="Insufficient monthly corporate balance")
    employee.monthly_balance -= expected_split["wallet_deducted"]

    db_txn = models.Transaction(
        employee_id=transaction.employee_id,
        total_cart_amount=transaction.total_cart_amount,
        wallet_deducted_amount=expected_split["wallet_deducted"],
        personal_paid_amount=expected_split["personal_paid"],
        items_list=transaction.items_list
    )
    db.add(db_txn)
    db.commit()
    db.refresh(db_txn)
    return db_txn

@router.get("/", response_model=List[schema.TransactionResponse])
def list_transactions(db: Session = Depends(get_db)):
    return db.query(models.Transaction).all()
