from fastapi import APIRouter

api_router = APIRouter()

# We will include endpoints here as we build them.
from .endpoints import menu
from .endpoints import hr_rules
from .endpoints import wallet
from .endpoints import transactions

api_router.include_router(menu.router, prefix="/pos/menu", tags=["menu"])
api_router.include_router(hr_rules.router, prefix="/hr/rules", tags=["hr_rules"])
api_router.include_router(wallet.router, prefix="/wallet", tags=["wallet"])
api_router.include_router(transactions.router, prefix="/transactions", tags=["transactions"])

