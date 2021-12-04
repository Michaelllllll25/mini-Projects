class BankAccount:
    def __init__(self, name: str, number: int, bank: str) -> None:
        self._name = name
        self._number = number
        self._bank = bank
        self._balance = 0

    def __str__(self):
        info = "Name: " + self._name + "\n"
        info += "Number: " + self._number + "\n"
        info += "Bank: " + self._bank + "\n"
        info += "Balance: " + str(self._balance)
        info += " " + "\n"
        return info

    # def __repr__(self):
    #     return str(self)

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        if len(name) > 15:
            raise ValueError("Name can not exceed 15 characters.")
        elif len(name) <= 0:
            raise ValueError("Name must be 1-15 characters.")
        self._name = name
        
    def get_number(self) -> int:
        return self._number

    def set_number(self, number: str) -> None:
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

    def withdraw(self, amount: int):
        if amount <= 0 or amount > self._balance:
            raise ValueError("Insuficient Funds")
        else:
            self._balance -= amount
            print("- $" + str(amount))
            print(f"Balance: ${self._balance}")
            print()
            

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Can not deposit a negative amount.")
        else:
            self._balance += amount
            print("+ $" + str(amount))
            print(f"Balance: ${self._balance}")
            print()

# account1 = BankAccount("Kenny", "12345678", "Python Bank")

# print(account1)

# account1.deposit(1000)

# account1.withdraw(750)






#TEST CODE
# account1 = BankAccount("Kenny", "12345678", "Python Bank")
# print(account1)

# #------- print(account1.set_name("Kennyyyyyyyyyyyyyyyyyyy"))
# # print(account1.set_name("Kenny"))

# #------- print(account1.set_number(str(123456789)))
# # print(account1.set_number(str(12345678)))

# #------- print(account1.set_bank("Pyth Bank"))
# # print(account1.set_bank("Python Bank"))

# #------- print(account1.set_balance(-1))
# # print(account1.set_balance(0))

# '''
# Name: Kenny
# Number: 12345678
# Bank: Python Bank
# Balance: 0
# '''

# # account1.deposit(1000)  # + $1000
# # # account1.withdraw(5000) # Withdraw Failed

# # # account1.deposit(-2000) # Deposit Failed
# # account1.deposit(5000)  # + $5000
# # account1.withdraw(750)  # - $750

# # print(account1)

# '''
# Name: Kenny
# Number: 12345678
# Bank: Python Bank
# Balance: 5250
# '''

# account1.deposit(1000)
# # account1.withdraw(3000)   # Withdraw failed

# # account1.deposit(-3000)   # Deposit failed
# account1.withdraw(750)

