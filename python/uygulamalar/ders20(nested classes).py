class Car:
    def __init__(self,brand,model,engine_hp,engine_fuel):
        self.brand=brand
        self.model=model
        self.engine=Car.Engine(engine_hp,engine_fuel)
    def show_details(self):
        print(f"Car:{self.brand} {self.model}")
        self.engine.show_engine()

    class Engine:
        def __init__(self,hp,fuel_type):
            self.type="V8"
            self.horse_power=hp
            self.fuel_type=fuel_type        
        def show_engine(self):
            print(f"Engine type:{self.type}\nEngine HorsePower:{self.horse_power} (HP)\nEngine Fuel Type:{self.fuel_type}")

c1=Car("Skoda","Superb",250,"Petro1")
c1.show_details()
