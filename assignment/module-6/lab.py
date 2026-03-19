# ================== lab - 1 ===============
# print('"hello , world !"')


# print("my name is Devanshi ")


# ================ lab - 2 ==================
# a=70
# b=50

# # a = (int(input("enther the number a ")))
# # print(a)

# # b = (int(input("enther the number b ")))
# # print(b)

# addition =(a+b)
# print(f"addition = {addition}")

# substract =(a-b)
# print(f"substract = {substract}")

# multiplication =(a*b)
# print(f"multiplication = {multiplication}")

# divison =(a/b)
# print(f"divison = {divison} ")

# modulo =(a%b)
# print(f"modulo = {modulo} ")

# flordivison =(a//b)
# print(f"flordivison = {flordivison} ")

# exponatiton =(a**3)
# print(f"exponatiton = {exponatiton} ")



# =================== lab - 3 ======================
# a=10
# print(type(a))

# a=12.5
# print(type(a))

# a = 4j + 5
# print(type(a))

# a= "Devanshi"
# print(type(a))

# a = ["tisha",12.5,"python",20]
# print(type(a))

# a = (10,20,50,60)
# print(type(a))

# a = {"age":20 , "date":2}
# print(type(a))

# a = {1,2,3,5,9}
# print(type(a))

# a = 10
# b = 9
# print(a > b)
# print(a == b)


# ======= practical - 1 =======
# a=10
# print(a)

# ======== practical - 2 =========
# name = "nilay"
# age = 28
# email = "nilay@gmail.com"

# print(name)
# print(age)
# print(email)

# ======== practical - 3 =======
# name = input("enter the name : ")
# print(name)

# ======= practical - 4 =======
# a = 20
# b = 19.54
# Name= "zinal"
# c=["param","mayur","hetal"]

# print(type(a))
# print(type(b))
# print(type(Name))
# print(type(c))

# ================== lab - 4 =====================
# ====== Que - 1 ======
# Number1=int(input("Enter the Number1 "))
# Number2=int(input("Enter the Number2 "))

# if Number1>Number2:
#     print(f"{Number1} is Greater than {Number2}") 
# else:
#     print(f"{Number2} is less than {Number1}") 

# ===== Que - 2 ======
# Number=int(input("Enter The Number:"))

# flag=1

# if flag==0:
#         print("number is prime")
# else:
#         print("number is not prime")

# ===== Que - 3 ====
# marks = int(input("enter the marks:"))

# if marks>=91 and marks<=100:
#         print("grade A")
# elif marks>=71 and marks<=90:
#         print("grade B")
# elif marks>=51 and marks<=70:
#         print("grade C")
# elif marks>=35 and marks<=50:
#         print("grade D")
# elif marks>=0 and marks<=34:
#         print("grade F")
# else :
#         print("invalid choice")  

# ======== Que - 4 =========
# age= int(input("Enter your age : "))

# if age>=18:
#     print("You can go to donate")
#     if age>=18:
#         print("You are eligible to donate blood")
# else:
#     print("You are not eligible to donate blood")
 

# ================== lab - 5 =======================
# ====== Que - 1 ======
# List1 = ['apple', 'banana', 'mango']
# for i in range(1):
#     print(List1)

# ======= Que - 2 ======
# List1 = ['apple', 'banana', 'mango']

# print(len(List1))

# for word in List1:
#     print(f"length of {word} is {len(word)}")

# ====== Que - 3 ======
# fruit= ['apple', 'banana', 'mango']
# search=input("Enter Your String:")

# for i in fruit:
#     if i==search:
#         print("string in the list")
#         break
#     else:
#         print("string is not in the list")

# ===== Que - 4 =====
# for i in range(5):
#     print("* "*(i+1))


# ====================== lab - 6 ==============================
# ====== Que - 1 =======
# def generate_even_numbers():
#     num = 0
#     count = 1
#     while count < 10:
#         yield num
#         num += 2
#         count += 1

# for even in generate_even_numbers():
#     print(even)

# ====== Que - 2 =======
# l = [10,20,30,40,50,60,70]
# k = iter(l)
# print(next(k))
# print(next(k))



# ====================== lab - 6 ==============================
# ====== Que - 1 =======
# print("hello")

# ====== Que - 2 =======
# b = "Hello, Python!"
# print(b)

# ====== Que - 3 =======
# print("""my name is devanshi..""")

# ====== Que - 4 =======
# x = "Python"
# print("First character:", x[0])

# ====== Que - 5 =======
# print("From second position onwards:", x[1:])

# ====== Que - 6 =======
# print("Up to fifth character:", x[:5])

# ====== Que - 7 =======
# print("Substring between index 1 and 4:", x[1:4])

# ====== Que - 8 =======
# print("Last character:", x[-1])

# ====== Que - 9 =======
# print("Alternate characters from index 1:", x[1::2])


#  ============================ lab - 8 ==============================
# ====== Que - 1 =======
# List1 = ['apple', 'banana', 'mango']
# for i in List1:
#     if i=="banana":
#         continue
#     print(i)

# ===== Que - 2 =====
# List1 = ['apple', 'banana', 'mango']
# for i in List1:
#     if i=="banana":
#         break
#     print(i)

# ======================= lab - 9 ============================
# ====== Que - 1 =======
# str="Hello Python!"
# print(str[1:])
# print(str[:5])
# print(str[5:9])
# print(str[-5:-2])
# print(str[::-1])

# ====== Que - 2 ======
# st= "my name is devanshi"
# print(len(st))

# st= "MY NAME IS devanshi"
# print(str.lower(st))

# st= "my name is devanshi"
# print(str.upper(st))

# st= "my name is devanshi"
# print(str.capitalize(st))

# st= "my name is devanshi"
# print(str.title(st))

# st= "  my name is devanshi   "
# print(st)
# print(st.strip())

# st= "my name is devanshi"
# print(st.replace('i','r',1))

# st= "my name is devanshi"
# print(st.find("devanshi"))

# st= "my name is devanshi"
# print(st.startswith("M"))

# st= "my name is devanshi"
# print(st.endswith("a"))

# st= "my name is devanshi"
# print(st.split(" ",2))

# print("XYZ".join("abc"))

# print("devanshi".isalpha())

# print("2005".isdigit())

# print("devanshi01".isalnum())

# print("zinal".zfill(50))

# print("zinal".center(50,"*"))



# ======================= lab - 10 ============================
# ====== Que - 1 =======
# def square (a):
#     return a*a
# x = [5,10,15,20,25,30]
# b = map(square,x)
# print(list(b))

# ====== Que - 2 =======
# x = [1,3,5,7,9,11]
# from functools import reduce
# k = reduce(lambda a,b:a*b,x)
# print(k)

# ====== Que - 3 =======
# l = [1,2,3,4,5,6,7,8,9,10]
# s = filter(lambda a : a%2==0,l)
# print(list(s))





#=========================================================== ASSESSMENT =============================================================================
#====================== simple calculator ============================
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Error!"
#     return a / b

# def modulo(a, b):
#     return a % b

# def Exponentiation(a, b):
#     return a ** b

# def Floor_division(a, b):
#     return a // b



# while True:
#     print("\n--- Calculator Menu ---")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. modulo")
#     print("6. Exponentiation")
#     print("7. Floor_division")

#     choice = input("Enter your choice (1-5): ")

#     if choice == "5":
#         print("Goodbye!")
#         break   

#     if choice in ["1", "2", "3", "4"]:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if choice == "1":
#             print("Result:", add(num1, num2))
#         elif choice == "2":
#             print("Result:", subtract(num1, num2))
#         elif choice == "3":
#             print("Result:", multiply(num1, num2))
#         elif choice == "4":
#             print("Result:", divide(num1, num2))
#         elif choice == "5":
#             print("Result:", modulo(num1, num2))
#         elif choice == "6":
#             print("Result:", Exponentiation(num1, num2))
#         elif choice == "7":
#             print("Result:", Floor_division(num1, num2))
#     else:
#         print("Invalid choice, try again.")






#====================== grade management system ============================
# choice="y"
# while choice != "n" :
#     marks=int(input("Enter the Marks:"))

#     if marks>=91 and marks<=100:
#         print("your grade is A")
#     elif marks>=71 and marks<=90:
#         print("your grade is B")
#     elif marks>=51 and marks<=70:
#         print("your grade is C")
#     elif marks>=35 and marks<=50:
#         print("your grade is D")
#     else:
#         print("fail ")

#     choice=input("do you want to continue?yes or no : ")




