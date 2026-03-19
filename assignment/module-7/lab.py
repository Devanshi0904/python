#===================================== Lab - 1 ============================================   
#==== Que - 1 =====
# a = [25, "python", 3.14, True, [1, 2, 3], {"name": "devanshi"}, (5, 10)]
# print(a)

#====== Que - 2 =====
# a = "my name is    lad "
# print(a[:10])
# print(a[::-1])
# print(a[2:9])
# print(a[:])
# print(a[-8:-1])
# print(a[9:])


#================== practical exmaple ====================
#====== Que - 1 =====
# list = [42,3.14,"devanshi",True,[1, 2, 3],(4, 5, 6),{"name": "tisha", "age": 20},{7, 8, 9}]
# print(list)

# for i in list:
#     print(list) 

#====== Que - 2 =====
# a = "my new car"
# print(len(a))




#============================================================= Lab - 2 =====================================================
#===== Que - 1 =====
# a = [10, 20, 30, 40]
# print(a)
# a.append(50)     
# print(a)

# a.insert(2, 25) 
# print(a)

#===== Que - 2 ======
# a.pop()
# print(a)

# a.remove(20)
# print(a)


#================== practical exmaple ====================
#===== Que - 1 =====
# a = ["tisha","zeel","rinkesh","ekta"]
# x = []
# for i in a:
#     if 'a' in i:
#         x.append(i)
# print(x)
 

# a.insert(4,50)
# print(a)


#===== Que - 2 =====
# a.pop(2)
# print(a)


# a.remove(20)
# print(a)




#============================================================= Lab - 3 =====================================================
#===== Que - 1 =====
# list = ["devanshi","zinal","hetal","nilay","mayur"]
# for i in list:
#     print(list)

#===== Que - 2 =====

# list.sort()
# print(list)

# x = sorted(list)
# print(x)




#================== practical exmaple ====================
#===== Que - 1 =====
# subject = ["python","C","java","sql"]
# for element in subject:
#     print(element)

#===== Que - 2 =====
# numbers = [] 
# for i in range(1, 6):
#     numbers.append(i)
# print( numbers)




#============================================================= Lab - 4 =====================================================
#===== Que - 1 =====
# a = (25, "Hello", 3.14, True, [1, 2, 3], {'a': 10, 'b': 20})
# print(a)

#===== Que - 2 =====
# a = (1,2,3,4,5)
# b=('a','b','c','d')
# c=a+b
# print(c)


#================== practical exmaple ====================
#===== Que - 1 =====
# number = [1, 2, 3, 4, 5]
# number = tuple(number)
# print(number)

#===== Que - 2 =====
# a = (10, "Hello", 3.14, True)
# print(a)

#===== Que - 3 =====
# x = ("eng","guj","hindi")
# y = ("python","java","CSS")
# z = x + y
# print(z)

#===== Que - 4 =====
# product = ("leptop","PC","tablet")
# print(product[1])





#============================================================= Lab - 5 =====================================================
#===== Que - 1 =====
# a = (10,20,30,40,50,60,70)
# print(a[1:6])

#===== Que - 2 =====
# x = (1,2,3,4,5,6,7)
# print(x[1:6:2])


#================== practical exmaple ====================
#===== Que - 1 =====
# person = ("devanshi","tisha","ekta","rinkesh","zeel","zinal","hetal","nilay")
# print(person[1:6])

#===== Que - 2 =====
# number = (1,3,5,7,9,11,13,15,17,19)
# print(number[-1])



#============================================================= Lab - 6 =====================================================
#===== Que - 1 =====
# student ={
#     "name":"devanshi",
#     "age":20,
#     "grade":'A',
#     "city":"surat",
#     "course":"web development",
#     "year":1,
# }
# print(student)

#===== Que - 2 =====
# print(student["name"])
# print(student["age"])
# print(student["grade"])
# print(student["city"])
# print(student["course"])
# print(student["year"])




#================== practical exmaple ====================
#===== Que - 1 =====
# fruits = {
#     "apple": "red",
#     "banana": "yellow",
#     "orange": "orange",
#     "mango": "golden"
# }
# print(fruits)

#===== Que - 2 =====
# print(fruits["apple"])
# print(fruits["banana"])
# print(fruits["orange"])
# print(fruits["mango"])





#============================================================= Lab - 7 =====================================================
#===== Que - 1 =====
# student["age"] = 26
# print(student)

#===== Que - 2 =====
# a = ["name","year","city"]
# b = ["zinal","2005","surat"]
# c={}
# for i in range (len(a)):
#     c[a[i]]=b
# print(c)
 
#================== practical exmaple ====================
#===== Que - 1 =====
# fruits["mango"]= "green"
# print(fruits)

#===== Que - 2 =====
# car = {
#     "brand": "Tesla",
#     "model": "Model 3",
#     "year": 2024,
#     "color": "White",
# }
# print(car.keys())
# print(car.values())

#===== Que - 3 =====
# a= [1,2,3]
# b= ['A','B','C']
# c={}
# for i in range (len(a)):
#     c[a[i]]=b
# print(c)

#===== Que - 4 =====
# from collections import Counter
# char_count = Counter("HELLO")
# print(dict(char_count))






#============================================================= Lab - 8 =====================================================
#===== Que - 1 =====
# def string(a):
#     print(a)
# x = input("Enter a string: ")
# print_string(x)

#===== Que - 2 =====
# a = int(input("enter the a : "))
# b = int(input("enter the b : "))
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b

# def divide(a,b):
#     return a/b

# def modulo(a,b):
#     return a%b

# def floor(a,b):
#     return a//b

# x = add(a,b)
# print("addition ", x)
# x = sub(a,b)
# print("subtraction ", x)
# x = mul(a,b)
# print("multiplication ", x)
# x = divide(a,b)
# print("divison ", x)
# x = modulo(a,b)
# print("modulo ", x)
# x = floor(a,b)
# print("floor divison ", x)



#================== practical exmaple ====================
#===== Que - 1 =====
# def string(a):
#     print(a)
# x = input("Enter a string: ")
# print_string(x)

#===== Que - 2 =====
# def add(a,b):
#     print(a+b)
# add(10,20)

#===== Que - 3 =====
# b = lambda a :a*a
# print(b(50))

#===== Que - 4 =====
# operation = lambda a, b: (a + b, a - b)
# result = operation(10, 5)
# print("Sum:", result[0])
# print("Difference:", result[1])




#============================================================= Lab - 9 =====================================================
#===== Que - 1 =====
# import math

# print(math.sqrt(25))
# print(math.ceil(10.1))
# print(math.floor(10.1))

#===== Que - 2 =====
# import random
# a = random.randint(10,30)
# print(a)




#================== practical exmaple ====================
#===== Que - 1 =====
# import math

# print(math.pow(10,2))
# print(math.floor(10.1))
# print(math.ceil(10.1))
# print(round(10.45))
# print(math.sqrt(25))

#===== Que - 2 =====
# import random
# a = random.randint(1,100)
# print(a)
