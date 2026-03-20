# ================ palindrome ===============
# n = int(input("enter the number"))
# n = 505
# temp = n
# sum = 0

# while n !=0:
#     rem = n%10
#     sum = sum*10+rem
#     n = n//10

# if sum==temp:
#     print("yes")
# else:
#     print("no")
# ======= palindrome without using temp =======
# a = "madam"
# if a==a[::-1]:
#     print("yes")
# else:
#     print("no")

# ========== fibonacci series ==========
# a = 20
# b = 21

# for i in range(5):
#     print(a)
#     c = a+b
#     a=b
#     b=c
# ======== using Recursion fibonacci ==========
# def fibonacci (n):
#     if n<=1:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)

# n = 5
# for i in range(5):
#     print(fibonacci(i) , end=" ")


# ============== factorial ================
# n = 5
# fact = 1

# while n!=0:
#     fact = fact*n
#     n-=1
# print(fact)
# ====== for loop ======
# n = 5
# fact=1

# for i in range (1,n+1):
#     fact = fact*i
# print(fact)
# ======= using Recursion factorial =======
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))


# ================== prime number ========================
# n = 8
# flag = 0

# for i in range(2,n):
#     if n%i==0:
#         flag=1
#         break
# if flag==0:
#     print("yes")
# else:
#     print("no")
# ======= numer print =======
# for n in range(1,11):
#     flag=0

#     for i in range(2,n):
#         if n%i==0:
#             flag=1
#             break

#     if flag ==0 and n>1:
#         print(n,end=" ")
# ======= without using flag =======
# for n in range(2,11):
    
#     for i in range(2,n):
#         if n%i == 0:
#             break
#     else:
#         print(n ,end=" ")


# ====================== armstong number =========================
# n = 153
# temp = n
# sum=0

# while n!=0:
#     rem = n%10
#     sum+=rem**3
#     n=n//10
# if(sum==temp):
#     print("yes")
# else:
#     print("no")
# ======= print number =======
# for n in range(1,1001):
#     temp=n
#     sum=0

#     while temp!=0:
#         rem = temp%10
#         sum+=rem**3
#         temp=temp//10
#     if sum==n:
#         print(n)


# ============================== count vowel and constant ===================================
# s = "hello devanshi"

# vowels = 0
# consonants = 0

# for ch in s:
#     if ch in "aeiouAEIOU":
#         vowels+=1
#     elif ch.isalpha(): 
#         consonants+=1

# print("vowels",vowels)
# print("consonant",consonants)
# ======== only vowel count =========
# s = "hello devanshi"
# count = 0
# vowels = "aeiouAEIOU"

# for ch in s:
#     if ch in vowels:
#         count+=1
# print("vowels:",count)


# ================================== swaping number ===============================
# a = 5
# b = 10

# a,b = b,a
# print("a ",a)
# print("b ",b)


# ==================== reverse string using silcing ======================
# str = "devanshi"
# reversed = str[::-1]
# print("reversed sting :",reversed)

# ======== reverse string without silcing =======
# s= "hello"
# reverse = " "

# for i in s:
#     reverse = i+reverse
# print("reversed string :",reverse)


# ===================== remove duplicate characters =======================
# str ="hello"
# result =" "

# for i in str:
#     if i not in result:
#         result+=i
# print("remove duplicate :",result)


# ========================= Anagram check ===========================
# s1 = "act"
# s2 = "cat"

# if sorted(s1)==sorted(s2):
#     print("yes")
# else:
#     print("no")


# ================== second large number ===================
# a = [12,51,2,6,91,88,56,32,45,78,96]
# a = list(set(a))
# a.sort()
# print(a[-2])


# =================== largest number in list =================
# a = [12,51,2,6,91,88,56,32,45,78,96]
# a = max(list(a))
# print("largest number:",a)


# ======================== version string increment and decrement ==============================
# version = "1.99.99"
# version = input("enter your version")

# a,b,c = map(int,version.split("."))

# c += 1

# if c == 100:
#     c = 0
#     b += 1/

# if b == 100:
#     b = 0
#     a += 1

# print(a,".",b,".",c,sep="")

# version = input("enter your version")

# a,b,c = map(int,version.split("."))

# c -= 1

# if c < 0:
#     c = 99
#     b -= 1

# if b < 0:
#     b = 99
#     a -= 1

# print(a,".",b,".",c,sep="")

 
# =================== sum of digit ==================
# num = 15
# sum = 0

# while num>0:
#     sum+=num%10
#     num//=10
# print(sum)

# ================== even or odd ======================
# num = 4
# if num %2 == 0:
#     print("yes")
# else:
#     print("no")

# =================== leap year =====================
# year = 2004
# if year%4==0:
#     print("yes")
# else:
#     print("no")


# ========================== multiplication num =================
# num = 15
# for i in range(1,11):
#     print(num,"X",i,"=",num*i)


