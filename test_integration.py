import pytest
from bank_app import transfer, calculate_interest


def test_transfer_success():
    balance_from, balance_to = transfer(5000, 2000, 1000)
    assert balance_from == 4000
    assert balance_to == 3000


def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(500, 2000, 1000)


def test_transfer_then_interest():
    balance_from, balance_to = transfer(6000, 2000, 1000)
    new_balance = calculate_interest(balance_to, 10, 1)
    assert new_balance == pytest.approx(3300.0)