from pydantic import BaseModel
from typing import Optional

class HRRuleBase(BaseModel):
    rule_text: str

class HRRuleCreate(HRRuleBase):
    pass

class HRRuleCompiled(BaseModel):
    id: int
    rule_text: str
    compiled_json: dict
    is_active: bool

    class Config:
        from_attributes = True
