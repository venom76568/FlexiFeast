from pydantic import BaseModel
from typing import Optional

class MenuItemBase(BaseModel):
    name: str
    price: float
    is_active: bool = True

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(MenuItemBase):
    name: Optional[str] = None
    price: Optional[float] = None
    is_active: Optional[bool] = None

class MenuItem(MenuItemBase):
    id: int

    class Config:
        from_attributes = True
