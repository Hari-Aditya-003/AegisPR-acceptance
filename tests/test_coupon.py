import pytest

from coupon import apply_coupon


def test_ordinary_discount() -> None:
    assert apply_coupon(100, 25) == 75


@pytest.mark.parametrize("total,discount", [(-1, 1), (1, -1)])
def test_negative_inputs_are_rejected(total: int, discount: int) -> None:
    with pytest.raises(ValueError):
        apply_coupon(total, discount)
