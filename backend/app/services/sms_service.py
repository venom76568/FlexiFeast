import logging
import random
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_otp() -> str:
    return str(random.randint(100000, 999999))

def send_otp_sms(phone_number: str, otp: str) -> bool:
    """
    Simulates sending an SMS.
    In a production environment, this would integrate with Twilio or Fast2SMS.
    """
    # Hybrid Sandbox Mode as chosen in PRD Decision
    from app.core.config import settings
    twilio_active = settings.TWILIO_ACTIVE
    
    if twilio_active:
        logger.info(f"Sending real SMS to {phone_number} with OTP: {otp}")
        # Insert Twilio client call here
        return True
    else:
        logger.info(f"[SANDBOX MODE] SMS to {phone_number} - Your OTP is: {otp}")
        return True
