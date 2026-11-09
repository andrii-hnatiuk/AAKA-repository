class Client:
    def __init__(self, client_id, balance, name):
        self.client_id = client_id
        self.balance = balance
        self.name = name

    def get_balance(self):
        return self.balance

    def pay(self, amount):
        if amount > 0:
            self.balance -= amount
        else:
            return False

    def add_balance(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def has_enough_balance(self, amount):
        return self.balance >= amount
