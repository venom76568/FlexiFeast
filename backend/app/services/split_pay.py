def calculate_split_payment(cart_total: float, daily_limit: float) -> dict:
    """
    Calculates the split payment logic based on HR rules.
    If the cart_total is within the daily_limit, the wallet pays the full amount.
    If it exceeds, the wallet pays up to the daily_limit, and the rest is paid personally.
    """
    if cart_total <= daily_limit:
        wallet_deducted = cart_total
        personal_paid = 0.0
    else:
        wallet_deducted = daily_limit
        personal_paid = cart_total - daily_limit

    return {
        "cart_total": cart_total,
        "wallet_deducted": wallet_deducted,
        "personal_paid": personal_paid
    }
