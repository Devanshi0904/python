# for i in range(1,20):
#     primeNumber = i
#     flag = 0
#     for i in range(2,primeNumber):
#         if primeNumber%i==0:
#             flag = 1
#             break
#     if flag==0:
#         print(f"prime number {primeNumber} ")
#     else:
#         pass








prime_number=5

flag = 0

for i in range(2,prime_number):
    if prime_number%i==0:
            flag = 1
            break
if flag==0:
        print(f"{prime_number} prime")
else:
        pass