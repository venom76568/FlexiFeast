from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class TransactionBase(BaseModel):
    employee_id: int
    total_cart_amount: float = Field(..., ge=0, description="Total cart value cannot be negative")
    wallet_deducted_amount: float = Field(..., ge=0, description="Wallet deduction cannot be negative")
    personal_paid_amount: float = Field(..., ge=0, description="Personal paid amount cannot be negative")
    items_list: List[Dict[str, Any]]

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
