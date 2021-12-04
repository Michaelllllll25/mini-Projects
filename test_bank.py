from bank import BankAccount


def test_bank_attributes():
    b = BankAccount("Kenny", "12345678", "Python Bank")
    assert b._name == "Kenny"
    assert b._number == "12345678"
    assert b._bank == "Python Bank"
    assert b._balance == 0

def test_get_name():
    b = BankAccount("Kenny", "12345678", "Python Bank")
    assert b._name == "Kenny"

def test_set_name():
    b = BankAccount("Kennyyyy", "12345678", "Python Bank")
    assert b._name == "Kennyyyy"

def test_get_number():
    b = BankAccount("Kenny", "12345678", "Python Bank")
    assert b._number == "12345678"

def test_set_number():
    b = BankAccount("Kenny", "12334", "Python Bank")
    assert b._number == "12334"

def test_get_bank():
    b = BankAccount("Kenny", "12345678", "Python Bank")
    assert b._bank == "Python Bank"

def test_set_bank():
    b = BankAccount("Kenny", "12345678", "Python Bankerrr")
    assert b._bank == "Python Bankerrr"

def test_get_balance():
    b = BankAccount("Kenny", "12345678", "Python Banker")
    assert b._balance == 0

def test_set_balance():
    b = BankAccount("Kenny", "12345678", "Python Banker")
    assert b._balance == 0   
