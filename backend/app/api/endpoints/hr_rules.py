from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.db import models
from app.schemas import hr_rules as schema
from app.core.ai_engine import parse_hr_rule

router = APIRouter()

@router.post("/", response_model=schema.HRRuleCompiled)
def create_hr_rule(rule: schema.HRRuleCreate, db: Session = Depends(get_db)):
    compiled_json = parse_hr_rule(rule.rule_text)
    db_rule = models.HRRule(rule_text=rule.rule_text, compiled_json=compiled_json)
    db.add(db_rule)
    db.commit()
    db.refresh(db_rule)
    return db_rule

@router.get("/", response_model=List[schema.HRRuleCompiled])
def get_hr_rules(db: Session = Depends(get_db)):
    return db.query(models.HRRule).all()
