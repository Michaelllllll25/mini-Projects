from credit import CreditCard

def test_credit_attributes():
    card = CreditCard("Kenny", "12345678", "Python Bank")
    assert card._name == "Kenny"
    assert card._number == "12345678"
    assert card._bank == "Python Bank"
    assert card._balance == 0
    assert card._limit == 8000

def test_get_name():
    card = CreditCard("Kenny", "12345678")
    assert card._name == "Kenny"

def test_set_name():
    card = CreditCard("Kennyyyy", "12345678")
    assert card._name == "Kennyyyy"

def test_get_number():
    card = CreditCard("Kenny", "12345678")
    assert card._number == "12345678"

def test_set_number():
    card = CreditCard("Kenny", "12334")
    assert card._number == "12334"

def test_get_bank():
    card = CreditCard("Kenny", "12345678", "Python Bank")
    assert card._bank == "Python Bank"

def test_set_bank():
    card = CreditCard("Kenny", "12345678", "Python Bankerrr")
    assert card._bank == "Python Bankerrr"

def test_get_balance():
    card = CreditCard("Kenny", "12345678")
    assert card._balance == 0

def test_set_balance():
    card = CreditCard("Kenny", "12345678")
    assert card._balance == 0   
