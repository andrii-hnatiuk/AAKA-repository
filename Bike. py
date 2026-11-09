REGULAR = "звичайний"
ELECTRIC = "електричний"

PRICES = {
    REGULAR: 2,
    ELECTRIC: 5,
}

class Bike:
    def init(self, bike_id, bike_type):
        self.bike_id = bike_id
        self.bike_type = bike_type

    def price_per_minute(self):
        return PRICES[self.bike_type]

    def calculate_cost(self, minutes):
        return self.price_per_minute() * minutes


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
