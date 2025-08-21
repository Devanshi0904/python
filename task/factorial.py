num=int(input("enter the number" ))   

for i in range (1,num+1):
        factorial = 1
        for j in range (1,i+1):
            factorial = factorial*j
        print(factorial)