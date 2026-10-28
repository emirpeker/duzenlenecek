class Return:
    def __init__(
        self, rental_id, return_date, return_odometer, penalty_fee, damage_fee
    ):
        self.rental_id = rental_id
        self.return_date = return_date
        self.return_odometer = return_odometer
        self.penalty_fee = penalty_fee
        self.damage_fee = damage_fee
