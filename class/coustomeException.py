# class AgeInvalidException(Exception):
#     pass

# def ageCheck(age):
#     if age <18:
#         raise AgeInvalidException("invalid age")
#     else:
#         print("valid age")

# try:
#     ageCheck(17)
# except Exception as e :
#     print(e)





class InsufficintAmountException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class bank :
    balance = 0

    def check_balance(self):
        print("current balance is :",self.balance)
    
    def deposite(self,amt):
        self.balance+=amt

    def withdrow(self,amt):
        if amt > self.balance:
            raise InsufficintAmountException(f"you need more {amt-self.balance} in your account to withrow")
        else:
            self.balance-=amt
b = bank()
b.check_balance()
b.deposite(80000)
b.check_balance()
try :
    b.withdrow(200000)
except Exception as e:
    print(e)
b.check_balance()











# class InvalidStringException(Exception):
#     def __init__(self, msg):
#         super().__init__(msg)

# def alphabet(str):
#     if str.isalpha():
#         print("valid")
#     else:
#         raise InvalidStringException("invalid")

# try:
#     alphabet("abca123")
# except Exception as e:
#     print(e)  