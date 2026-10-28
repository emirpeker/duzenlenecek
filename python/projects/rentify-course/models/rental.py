# models/rental.py

from datetime import date
from typing import Optional


class Rental:
    def __init__(
        self,
        id: int,
        car_id: int,
        customer_id: int,
        start_date: date,
        planned_end_date: date,
        actual_return_date: Optional[date],
        start_odometer: int,
        total_price: float,
    ):
        self.id = id
        self.car_id = car_id
        self.customer_id = customer_id
        self.start_date = start_date
        self.planned_end_date = planned_end_date
        self.actual_return_date = actual_return_date
        self.start_odometer = start_odometer
        self.total_price = total_price

    @property
    def is_active(self) -> bool:
        return self.actual_return_date is None
