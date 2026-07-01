# sample test cases for the calculations module

import pytest
from app.calculations import add, subtract, multiply, divide, BankAccount


@pytest.fixture()
def zero_bank_account():
    print("creating empty bank account")
    return BankAccount(0)

@pytest.fixture()
def bank_account():
    return BankAccount(100)

@pytest.mark.parametrize("num1, num2, expected", 
                         [(5, 2, 7), 
                          (10, 2, 12), 
                          (0, 0, 0)])

# def test_add():
#     print("testing add function")
#     assert add(5, 2) == 7

def test_add(num1, num2, expected):
    print("testing add function")
    assert add(num1, num2) == expected
    
def test_subtract():
    print("testing subtract function")
    assert subtract(5, 2) == 3
    
def test_multiply():
    print("testing multiply function")
    assert multiply(5, 2) == 10
    
def test_divide():
    print("testing divide function")
    assert divide(10, 2) == 5

    
def test_bank_set_initial_balance():
    bank_account = BankAccount(100)
    assert bank_account.balance == 100
    
def test_bank_default_amount(zero_bank_account):
    # bank_account = BankAccount()
    print("testing bank account with default amount")
    assert zero_bank_account.balance == 0
    
def test_withdraw():
    bank_account = BankAccount(100)
    bank_account.withdraw(50)
    assert bank_account.balance == 50
    
def test_deposit():
    bank_account = BankAccount(100)
    bank_account.deposit(50)
    assert bank_account.balance == 150
    
def test_collect_interest():
    bank_account = BankAccount(100)
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 110