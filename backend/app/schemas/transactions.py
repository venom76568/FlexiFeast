from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime

class TransactionBase(BaseModel):
    employee_id: int
    total_cart_amount: float
    wallet_deducted_amount: float
    personal_paid_amount: float
    items_list: List[Dict[str, Any]]

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
