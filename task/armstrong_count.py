for i in rang(100,1000)
num=i
temp = num
sum=0

for i in range (100,1000):
    amrstrong = i 

    rem = num %10
    sum +=rem**3
    num = num//10

if (sum==temp):
    print(f"{temp} armstrong ")
else:
    print(f"{temp} not armstrong ")
