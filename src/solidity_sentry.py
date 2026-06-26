import json
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class Seat:
    id: int
    usage: int

@dataclass
class Billing:
    seats: list
    next_billing_date: str
    projected_monthly_cost: float

class SoliditySentry:
    def __init__(self):
        self.seats = []
        self.billing_history = []

    def add_seat(self, seat):
        self.seats.append(seat)
        self.billing_history.append({"action": "add", "seat_id": seat.id})

    def remove_seat(self, seat_id):
        self.seats = [seat for seat in self.seats if seat.id != seat_id]
        self.billing_history.append({"action": "remove", "seat_id": seat_id})

    def get_billing(self):
        next_billing_date = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
        projected_monthly_cost = len(self.seats) * 10.0
        return Billing(self.seats, next_billing_date, projected_monthly_cost)

    def log_billing_action(self, action, seat_id):
        self.billing_history.append({"action": action, "seat_id": seat_id})

    def get_billing_history(self):
        return self.billing_history
