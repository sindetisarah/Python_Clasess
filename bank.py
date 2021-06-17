from datetime import datetime
class BankAccount:
    def __init__(self,name,phone_number):
        self.name=name,
        self.phone_number=phone_number
        self.balance=0
        self.loan=0
        self.statement=[]
    def show_balance(self):
        return f"Hello {self.name} your balance is {self.balance}"
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            now=datetime.now()
            formated_datetime=now.strftime("%d/%m/%Y %H:%M:%S")
            transaction={
                "amount":amount,
                "time":formated_datetime,
                "Narration":"You hava deposited"
            }
            self.statement.append(transaction)
            return self.show_balance()
        else:
            return f"Dear Customer {self.name} your amount is negative"

    def withdraw(self,amount):
        if self.balance<amount:
            return "Sorry you do not have enough money in your account"
        else:
            self.balance-=amount
            now=datetime.now()
            transaction={
                "amount":amount,
                "time":now,
                "Narration":"Confirmed withdrawn  {amount} at KCB bank and your new Mpesa balance is {self.balance}"

            }
            self.statement.append(transaction)
            return self.show_balance()
    """
    Borrowing a loan
    """
    def borrow(self,amount):
        self.loan+=amount
        return f"Hello {self.name} you have now borrowed a loan of{self.loan} Ksh"
    """
    Paying the loan
    """
    def pay_loan(self,amount):
        self.loan-=amount
        