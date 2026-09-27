"""Order pricing helpers for the orders-api service."""


def order_total(items):
    """Return the total price for a list of (quantity, unit_price) pairs."""
    return round(sum(qty * price for qty, price in items), 2)
