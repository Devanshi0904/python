num=525
temp = num
sum =0

while num !=0:
    rem = num%10
    sum = sum*10 +rem
    num = num//10

if sum==temp:
    print("palindrom")
else:
    print("not palindrome")