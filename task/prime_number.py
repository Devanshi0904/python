
for j in range(3,100):
    prime_number=j

    flag = 0

    for i in range(2,prime_number):
        if prime_number%i==0:
            flag = 1
            break
    if flag==0:
        print(f"{prime_number} prime")
    else:
        pass
       



#even or odd
# if num%2==0

# leap year
# if year%4==0

