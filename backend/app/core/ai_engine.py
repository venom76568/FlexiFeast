import json
import re

def parse_hr_rule(text: str) -> dict:
    """
    Mock AI Engine parser.
    Converts plain english rules like 'Limit daily spend to 250' to JSON structure.
    """
    text_lower = text.lower()
    result = {"type": "unknown"}
    
    if "limit" in text_lower and "daily" in text_lower:
        match = re.search(r'\d+', text)
        if match:
            result = {
                "type": "daily_limit",
                "value": float(match.group())
            }
            
    return result
