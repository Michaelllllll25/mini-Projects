class CreditCard:
    def __init__(self, name, number, bank = "Python Bank"):
        self._name = name
        self._number = number
        self._bank = bank
        self._balance = 0
        self._limit = 8000

    def __str__(self):
        info = "Name: " + self._name + "\n"
        info += "Number: " + "XXXX" + self._number[4:] + "\n"
        info += "Bank: " + self._bank + "\n"
        info += "Balance: " + str(self._balance)
        return info
    
    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        if len(name) > 15:
            raise ValueError("Name can not exceed 15 characters.")
        elif len(name) <= 0:
            raise ValueError("Name must be 1-15 characters.")
        self._name = name

    def get_number(self) -> int:
        return self.number

    def set_number(self, number: int) -> None:
        if len(number) != 8:
            raise ValueError("INVALID BANK NUMBER.")
        self._number = number

    def get_bank(self) -> str:
        return self._bank

    def set_bank(self, bank: int) -> None:
        if bank != "Python Bank":
            raise ValueError("Wrong Bank")
        self._bank = bank

    def get_balance(self) -> int:
        return self._balance

    def set_balance(self, balance: int) -> None:
        if balance < 0:
            raise ValueError("Pay your debits, you have a negative balance.")
        self._balance = balance

    def get_limit(self):
        return self._limit

    def set_limit(self, limit: int) -> None:
        if self._limit < 0:
            raise ValueError("INVALID LIMIT.")
        self._limit = limit

    def charge(self, amount: int) -> None:
        #not int or not not float
        if not (isinstance(amount, int) or  isinstance(amount, float)) or (amount <= 0):
            raise ValueError("Charge Denied")
        else:
            self._balance += amount
    
    def pay(self, amount: int) -> None:
        if not (isinstance(amount, int) or  isinstance(amount, float)) or (amount <= 0):
            raise ValueError("Charge Denied")
        else:
            self._balance -= amount




# card = CreditCard("Kenny", "12345678")
# print(card)
# card.charge(10000)
# print(card)
# card.charge(200)
# print(card)

# card.pay(5000)
# print(card)
