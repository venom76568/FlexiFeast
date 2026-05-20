import json
import logging
import re
import os

from app.services.swiggy_mcp import search_items, build_cart_deeplink

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_chatbot_order(message: str, employee_daily_limit: float) -> dict:
    """
    Core Slack/Teams chatbot order handler.
    1. Searches menu based on natural language
    2. Calculates split-payment if total exceeds budget
    3. Returns response dict with instruction for the bot to send
    """
    found_items = search_items(message)

    if not found_items:
        return {
            "type": "no_match",
            "message": "Sorry, I couldn't find that item in today's menu. Try 'show menu' to see available options."
        }

    cart_total = sum(i["price"] for i in found_items)
    item_ids = [i["id"] for i in found_items]
    deeplink = build_cart_deeplink(item_ids)

    if cart_total <= employee_daily_limit:
        return {
            "type": "approved",
            "message": (
                f"Found: *{', '.join(i['name'] for i in found_items)}* "
                f"(Total: ₹{cart_total}). "
                f"Your corporate wallet covers the full amount. "
                f"[Order on Swiggy]({deeplink})"
            ),
            "wallet_deducted": cart_total,
            "personal_paid": 0,
            "deeplink": deeplink
        }
    else:
        personal_due = cart_total - employee_daily_limit
        return {
            "type": "split",
            "message": (
                f"Found: *{', '.join(i['name'] for i in found_items)}* "
                f"(Total: ₹{cart_total}). "
                f"Your daily limit is ₹{employee_daily_limit}. "
                f"Wallet covers ₹{employee_daily_limit}, you pay ₹{personal_due} on Swiggy. "
                f"Reply *YES* to proceed: [Order on Swiggy]({deeplink})"
            ),
            "wallet_deducted": employee_daily_limit,
            "personal_paid": personal_due,
            "deeplink": deeplink
        }
