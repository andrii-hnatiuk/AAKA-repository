def take_bike(station):
    bike = station.take_bike()
    if bike is None:
        return None
    return bike

def count_costs(bike, minutes):
    if bike.bike_type == "normal":
        price_per_minute = 2
    else:
        price_per_minute = 5
    return minutes * price_per_minute

def block_bike_if_no_balance(client, bike, amount):
    if not client.has_enough_balance(amount):
        if hasattr(bike, "lock_wheels"):
            bike.lock_wheels()
        return True
    return False

def return_bike(client, bike, station, minutes):
    cost = count_costs(bike, minutes)
    if not client.has_enough_balance(cost):
        if hasattr(bike, "lock_wheels"):
            bike.lock_wheels()
        return None

    client.pay(cost)
    station.return_bike(bike)

    return cost

def whole_sum(total, amount):
    return total + amount
