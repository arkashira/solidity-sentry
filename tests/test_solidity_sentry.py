from datetime import datetime, timedelta
from solidity_sentry import SoliditySentry, Seat, Billing

def test_add_seat():
    sentry = SoliditySentry()
    seat = Seat(1, 10)
    sentry.add_seat(seat)
    assert len(sentry.seats) == 1
    assert sentry.seats[0].id == 1

def test_remove_seat():
    sentry = SoliditySentry()
    seat = Seat(1, 10)
    sentry.add_seat(seat)
    sentry.remove_seat(1)
    assert len(sentry.seats) == 0

def test_get_billing():
    sentry = SoliditySentry()
    seat = Seat(1, 10)
    sentry.add_seat(seat)
    billing = sentry.get_billing()
    assert len(billing.seats) == 1
    assert billing.next_billing_date == (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
    assert billing.projected_monthly_cost == 10.0

def test_log_billing_action():
    sentry = SoliditySentry()
    sentry.log_billing_action("add", 1)
    assert len(sentry.get_billing_history()) == 1
    assert sentry.get_billing_history()[0]["action"] == "add"
    assert sentry.get_billing_history()[0]["seat_id"] == 1

def test_get_billing_history():
    sentry = SoliditySentry()
    sentry.log_billing_action("add", 1)
    sentry.log_billing_action("remove", 2)
    assert len(sentry.get_billing_history()) == 2
    assert sentry.get_billing_history()[0]["action"] == "add"
    assert sentry.get_billing_history()[1]["action"] == "remove"
