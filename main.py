from Bike import Bike, Station, REGULAR, ELECTRIC, Client
#from ... import ...
#from ... import ...

def main():
    print("Запуск демонстрації")
    
    print("\nСтворення станцій.")
    station1 = Station("Центральна")
    station2 = Station("Паркова")
    print(f"Створено станції: '{station1.name}' та '{station2.name}'")

    print("\nСтворення та розподіл велосипедів")
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


    print("Демонстрацію завершено")


if __name__ == "__main__":
    main()
