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
    bike3 = Bike(bike_id="E-01", bike_type=ELECTRIC)
    bike4 = Bike(bike_id="E-02", bike_type=ELECTRIC)
    bike5 = Bike(bike_id="R-03", bike_type=REGULAR)

    station1.add_bike(bike1)
    station1.add_bike(bike2)
    station1.add_bike(bike3)
    station2.add_bike(bike4)
    station2.add_bike(bike5)
    
    print(f"На станцію '{station1.name}' додано 3 велосипеди.")
    print(f"На станцію '{station2.name}' додано 2 велосипеди.")

    print("\n--- Крок 3: Створення клієнтів ---")
    client1 = Client(client_id=1, balance=400, name="Олександр")
    client2 = Client(client_id=2, balance=150, name="Марія")
    print(f"Клієнт 1: {client1.name}, баланс: {client1.get_balance()} грн")
    print(f"Клієнт 2: {client2.name}, баланс: {client2.get_balance()} грн")
    
    print("\nКрок 4: Виконання поїздок")
    
    b1 = take_bike(station1)
    if b1:
        cost1 = return_bike(client1, b1, station2, minutes=20)
        if cost1 is not None:
            total_network_revenue = whole_sum(total_network_revenue, cost1)
            print(f"Поїздка 1: {client1.name} проїхав 20 хв. Списано {cost1} грн.")
            
    b2 = take_bike(station1)
    if b2:
        cost2 = return_bike(client2, b2, station2, minutes=10)
        if cost2 is not None:
            total_network_revenue = whole_sum(total_network_revenue, cost2)
            print(f"Поїздка 2: {client2.name} проїхала 10 хв. Списано {cost2} грн.")

    b3 = take_bike(station2)
    if b3:
        cost3 = return_bike(client1, b3, station1, minutes=15)
        if cost3 is not None:
            total_network_revenue = whole_sum(total_network_revenue, cost3)
            print(f"Поїздка 3: {client1.name} проїхав 15 хв. Списано {cost3} грн.")

    print("\nКрок 5: Перевірка ситуації, коли на станції немає велосипедів")
    empty_station = Station("Пуста станція")
    print(f"Пробуємо взяти велосипед зі станції '{empty_station.name}', де 0 велосипедів:")
    
    missing_bike = take_bike(empty_station)
    if missing_bike is None:
        print("[Повідомлення]: Вибачте, на цій станції зараз немає вільних велосипедів!")

    print("\n--- Крок 6: Баланс клієнтів після поїздок ---")
    print(f"Баланс клієнта {client1.name}: {client1.get_balance()} грн")
    print(f"Баланс клієнта {client2.name}: {client2.get_balance()} грн")

    print("\n--- Крок 7: Звіт адміністратора ---")
    print(f"Станція '{station1.name}': {station1.count_bikes()} велосипедів.")
    print(f"Станція '{station2.name}': {station2.count_bikes()} велосипедів.")
    print(f"Станція '{empty_station.name}': {empty_station.count_bikes()} велосипедів.")
    print(f"Загалом мережа заробила: {total_network_revenue} грн")
    
    print("\nДЕМОНСТРАЦІЮ ЗАВЕРШЕНО УСПІШНО")

if __name__ == "__main__":
    main()
