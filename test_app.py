from app import order_total


def test_order_total_sums_line_items():
    assert order_total([(2, 4.50), (1, 10.00)]) == 19.00


def test_order_total_empty_order_is_zero():
    assert order_total([]) == 0
