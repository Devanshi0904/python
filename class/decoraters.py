# def beforeTest(test):
#     def wrapper():
#         print("call before test...")
#         test()
#     return wrapper

# @beforeTest
# def test():
#     print("test calling ...")

# @beforeTest
# def demo():
#     print("demo calling ...")
# test()
# demo()




# def add(calc):
#     def wrapper(*a):
#         print(a[0]+a[1])
#         calc(*a)
#     return wrapper

# def mul(calc):
#     def wrapper(*a):
#         print(a[0]*a[1])
#         calc(*a)
#     return wrapper
# @mul
# @add
# def calc(a,b):
#     print("calc operation ")
# calc(10,20)


x = [1,2,3,]*2
print(x)



# def onlyNumber(func):
#     def wrapper(*a):
#         if not str(a[0]).isdigit():
#             print("only number allowed")
#         else:
#             func(*a)
#     return wrapper


# def onlycharcter(func):
#     def wrapper(*a):
#         if not str(a[0]).isalpha():
#             print("only charter allowed")
#         else:
#             func(*a)
#     return wrapper


# def onlyNumAlpha(func):
#     def wrapper(*a):
#         if not str(a[0]).isalnum():
#             print("only number and chater allowed")
#         else:
#             func(*a)
#     return wrapper
    


# @onlyNumAlpha
# def myfunc(a):
#     print(a)

# myfunc("@")
