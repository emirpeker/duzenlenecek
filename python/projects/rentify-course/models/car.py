class Car:
    def __init__(
        self,
        id: int,
        plate_number: str,
        brand: str,
        model: str,
        daily_price: float,
        status: str,
        kilometer: int = 0,
    ):
        self.id = id
        self.plate_number = plate_number
        self.brand = brand
        self.model = model
        self.daily_price = daily_price
        self.status = status
        self.kilometer = kilometer

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            plate_number=data["plate_number"],
            brand=data["brand"],
            model=data["model"],
            daily_price=data["daily_price"],
            status=data["status"],
            kilometer=data.get("kilometer", 0),
        )

    def is_available(self) -> bool:
        return self.status == "available"
