# from abc import ABC,abstractmethod


# class Demo(ABC):

#     @abstractmethod
#     def test(self):
#         pass

# class DemoImp(Demo):

#     def test(self):
#         print("test calling...")
   

# # d  =Demo()
# # d.test()

# d = DemoImp()
# d.test()










# from abc import ABC,abstractmethod

# class account(ABC):

#     balance = 0
#     @abstractmethod
#     def deposite(self,amt):
#         pass
#     @abstractmethod
#     def withdraw(self,amt):
#         pass

#     def getbalance(self):
#         print("current balance is :",self.balance)

# class saving(account):
#     def deposite(self, amt):
#         self.balance+=amt

#     def withdraw(self, amt):
#         if amt >self.balance:
#             print("insufficinet amount")
#         else:
#             self.balance-=amt

# class loan (account):
#     def deposite(self, amt):
#         self.balance-=amt
    
#     def withdraw(self, amt):
#         self.balance+=amt
    
# s = saving()
# s.getbalance()
# s.deposite(5000)
# s.deposite(3000)
# s.getbalance()
# s.withdraw(5000)
# s.getbalance()

# print("*********************************")
# l = loan()
# l.getbalance()
# l.withdraw(500000)
# l.getbalance()
# l.deposite(400000)
# l.getbalance()