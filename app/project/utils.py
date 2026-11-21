def calculate_discount(price: float, discount: float) -> float:
    """Calculate price after applying a discount."""
    return price - (price * discount / 100)


def is_even(number: int) -> bool:
    """Check if a number is even."""
    return number % 2 == 0


def get_full_name(first_name: str, last_name: str) -> str:
    """Return a full name."""
    return f"{first_name} {last_name}"
