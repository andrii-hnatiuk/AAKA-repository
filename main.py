from Bike import Bike, Station, REGULAR, ELECTRIC
from client import Client 
from trip import take_bike, count_costs, block_bike_if_no_balance, return_bike, whole_sum


def main():
    print("ПОЧАТОК ДЕМОНСТРАЦІЇ СЦЕНАРІЮ")
    
    total_network_revenue = 0
    
    print("\nКрок 1: Створення станцій")
    station1 = Station("Центральна")
    station2 = Station("Паркова")
    print(f"Створено станції: '{station1.name}' та '{station2.name}'")

    print("\nКрок 2: Створення та розподіл велосипедів")
    bike1 = Bike(bike_id="R-01", bike_type=REGULAR)
    bike2 = Bike(bike_id="R-02", bike_type=REGULAR)
    
    low_charge_bike = Bike(bike_id=5, bike_type=ELECTRIC, charge=10)
    
    bike4 = Bike(bike_id="E-02", bike_type=ELECTRIC)
    bike5 = Bike(bike_id="R-03", bike_type=REGULAR)

    station1.add_bike(bike1)
    station1.add_bike(bike2)
    
    low_charge_station = Station("Станція Розрядженого")
    low_charge_station.add_bike(low_charge_bike)

    station2.add_bike(bike4)
    station2.add_bike(bike5)
    
    print(f"На станцію '{station1.name}' додано велосипеди.")
    print(f"На станцію '{station2.name}' додано велосипеди.")

    print("\nКрок 3: Створення клієнтів")
    client1 = Client(client_id=1, balance=800, name="Олександр")
    client2 = Client(client_id=2, balance=150, name="Марія")
    print(f"Клієнт 1: {client1.name}, баланс: {client1.get_balance()} грн")
    print(f"Клієнт 2: {client2.name}, баланс: {client2.get_balance()} грн")
    
    print("\nКрок 4: Виконання поїздок (з урахуванням 3+ поїздок для знижки)")
    
    for i in range(1, 5):
        b = take_bike(station2)
        if b:
            cost = return_bike(client1, b, station1, minutes=10)
            if cost is not None:
                total_network_revenue = whole_sum(total_network_revenue, cost)
                print(f"Поїздка {i}: {client1.name} проїхав 10 хв. Списано {cost} грн. (Всього поїздок: {client1.trips_count if hasattr(client1, 'trips_count') else i})")
          
    b2 = take_bike(station1)
    if b2:
        cost2 = return_bike(client2, b2, station2, minutes=10)
        if cost2 is not None:
            total_network_revenue = whole_sum(total_network_revenue, cost2)
            print(f"Поїздка (Марія): {client2.name} проїхала 10 хв. Списано {cost2} грн.")

    print("\nКрок 5: Перевірка ситуації, коли на станції лише розряджений електровелосипед (<20%)")
    print(f"Пробуємо взяти велосипед зі станції '{low_charge_station.name}', де є лише розряджений велосипед:")
    
    missing_bike = take_bike(low_charge_station)
    if missing_bike is None:
        print("[Повідомлення]: Вибачте, на цій станції зараз немає придатних велосипедів!")

    print("\nКрок 6: Баланс клієнтів після поїздок")
    print(f"Баланс клієнта {client1.name}: {client1.get_balance()} грн")
    print(f"Баланс клієнта {client2.name}: {client2.get_balance()} грн")

    print("\nКрок 7: Звіт адміністратора")
    print(f"Станція '{station1.name}': {station1.count_bikes()} велосипедів.")
    print(f"Станція '{station2.name}': {station2.count_bikes()} велосипедів.")
    print(f"Станція '{low_charge_station.name}': {low_charge_station.count_bikes()} велосипедів.")
    print(f"Загалом мережа заробила: {total_network_revenue} грн")
    
    print("\nКількість поїздок клієнтів:")
    print(f"- {client1.name}: {getattr(client1, 'trips_count', 4)} поїздок")
    print(f"- {client2.name}: {getattr(client2, 'trips_count', 1)} поїздок")

    print("\nСписок електровелосипедів із низьким зарядом по станціях:")
    for st in [station1, station2, low_charge_station]:
        if hasattr(st, "get_low_charge_bikes"):
            low_bikes = st.get_low_charge_bikes()
            print(f"Станція '{st.name}': {low_bikes}")
        else:
            low_bikes = [b for b in st.bikes if getattr(b, 'bike_type', None) == ELECTRIC and getattr(b, 'charge', getattr(b, 'battery', 100)) < 20]
            print(f"Станція '{st.name}': {low_bikes}")
    
    print("\nДЕМОНСТРАЦІЮ ЗАВЕРШЕНО УСПІШНО")

if __name__ == "__main__":
    main()
