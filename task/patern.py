# for j in range(5):
#         print("*"*5)


# for i in range(5):
#     for j in range(i+1):
#         print("*",end="")
#     print()


print("============= left up ===========")

for i in range(5):
    print("*"*(i+1))

print("============ left down ============")

for i in range (5,0,-1):
    print("*"*i)

print("==========right down ==========")

for i in range (5,0,-1):
    print(' '*(5-i)+'*'*i)

print("============ right up =========")

for i in range (1,6):
    print(' '*(5-i)+'*'*i)

