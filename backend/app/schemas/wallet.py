from pydantic import BaseModel
from typing import Optional

class EmployeeBase(BaseModel):
    name: str
    phone: str
    daily_limit: float = 250.0
    monthly_balance: float = 5000.0
    is_active: bool = True

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    daily_limit: Optional[float] = None
    monthly_balance: Optional[float] = None
    is_active: Optional[bool] = None

class Employee(EmployeeBase):
    id: int

    class Config:
        from_attributes = True
