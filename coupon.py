"""Tiny checkout rule used solely for the AegisPR acceptance fixture."""


def apply_coupon(total: int, discount: int) -> int:
    """Apply a nonnegative discount without allowing a negative checkout total."""
    if total < 0 or discount < 0:
        raise ValueError("total and discount must be nonnegative")
    return total - discount
