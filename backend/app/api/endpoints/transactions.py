from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.db import models
from app.schemas import transactions as schema

router = APIRouter()

@router.post("/", response_model=schema.TransactionResponse)
def create_transaction(transaction: schema.TransactionCreate, db: Session = Depends(get_db)):
    db_txn = models.Transaction(
        employee_id=transaction.employee_id,
        total_cart_amount=transaction.total_cart_amount,
        wallet_deducted_amount=transaction.wallet_deducted_amount,
        personal_paid_amount=transaction.personal_paid_amount,
        items_list=transaction.items_list
    )
    db.add(db_txn)
    db.commit()
    db.refresh(db_txn)
    return db_txn

@router.get("/", response_model=List[schema.TransactionResponse])
def list_transactions(db: Session = Depends(get_db)):
    return db.query(models.Transaction).all()
