from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .session import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone = Column(String, unique=True, index=True)
    daily_limit = Column(Float, default=250.0)
    monthly_balance = Column(Float, default=5000.0)
    is_active = Column(Boolean, default=True)

    transactions = relationship("Transaction", back_populates="employee")

class CanteenMenu(Base):
    __tablename__ = "canteen_menu"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    is_active = Column(Boolean, default=True)

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    total_cart_amount = Column(Float)
    wallet_deducted_amount = Column(Float)
    personal_paid_amount = Column(Float)
    items_list = Column(JSON) # Store list of item dicts
    created_at = Column(DateTime, default=datetime.utcnow)

    employee = relationship("Employee", back_populates="transactions")

class HRRule(Base):
    __tablename__ = "hr_rules"

    id = Column(Integer, primary_key=True, index=True)
    rule_text = Column(String)
    compiled_json = Column(JSON)
    is_active = Column(Boolean, default=True)
