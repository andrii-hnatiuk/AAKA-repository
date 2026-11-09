REGULAR = "звичайний"
ELECTRIC = "електричний"

PRICES = {
    REGULAR: 2,
    ELECTRIC: 5,
}

LOW_CHARGE = 20

class Bike:
    def __init__(self, bike_id, bike_type, charge=100): 
        self.bike_id = bike_id
        self.bike_type = bike_type
        self.charge = charge #
        self.wheels_locked = False

    def price_per_minute(self):
        return PRICES[self.bike_type]

    def calculate_cost(self, minutes):
        return self.price_per_minute() * minutes

    def lock_wheels(self):
        self.wheels_locked = True
        return True

    def is_low_charge(self): #
        return self.bike_type == ELECTRIC and self.charge < LOW_CHARGE

    def is_available(self): #
        return not self.is_low_charge()

    


class Station:

    def __init__(self, name):
        self.name = name
        self.bikes = []

    def add_bike(self, bike):
        self.bikes.append(bike)

    def count_bikes(self):
        return len(self.bikes)

    def take_bike(self, bike_type=None):
        for bike in self.bikes:
            if bike_type is None or bike.bike_type == bike_type:
                self.bikes.remove(bike)
                return bike
        return None

    def return_bike(self, bike):
        self.bikes.append(bike)

    def get_low_charge_bikes(self): #
        result = []
        for bike in self.bikes:
            if bike.is_low_charge():
                result.append((bike.number, self.name, bike.charge))
        return result
