#================================================== Que - 1 ======================================================================
#====== lab - 1 ======
# print("hello , my name is devanshi")
# name = "tisha"
# city = "surat"
# print(f"my name is {name} , i live in {city}")

#======== Practical Example ==========
#====== lab - 1 =====
# print('"hello , world!"')


#================================================== Que - 2 ======================================================================
#====== lab - 1 ======
# name = input("enter your name :")
# age = int(input("enter youe age :"))
# print(f"my name is {name} , my age is {age}")

#======== Practical Example ==========
#====== lab - 2 =====
# product = input("enter your product name :")
# price = int(input("enter your price :"))
# tax = float(input("enter the tax :"))

# print("\n=== product details ===")
# print("product ",product)
# print("price :",price)
# print("tax :",tax)


#================================================== Que - 3 ======================================================================
#====== lab - 1 ======
# f = open("test.txt",'w')                
# f.write("hello , i am python student ")
# f.close()

#======== Practical Example ==========
#====== lab - 3 ======
# a = open("study.txt",'w')
# a.write("puthon subject is very easy but situational programing language")
# a.close()


#================================================== Que - 4 ======================================================================
#====== lab - 1 ======
# f = open("test.txt",'r')                 
# data = f.read()
# print(data)

#====== lab - 2 ======
# a = open("self.txt",'w')
# a.write("my self devanshi \n")
# a.write("i am basically from surat \n")
# a.write("that's all about my self \n")
# a.close()

#======== Practical Example ==========
#====== lab - 4 ======
# d = open("string.txt",'w')
# d.write("this is my string")
# d.close()

#====== lab - 5 ======
# d = open("string.txt",'r')
# data = d.read()
# print(data)

#====== lab - 6 ======
# with open('string.txt','r')as d:
#     data = d.read()
#     print(d.tell())
#     print(data)


#================================================== Que - 5 ======================================================================
#====== lab - 1 ======
# try:
#     a = float(input("Enter the value a : "))
#     b = float(input("Enter the value b : "))
#     op = input("Enter operation (+, -, *, /): ")

#     if op == '+':
#         print("Result:", a + b)
#     elif op == '-':
#         print("Result:", a - b)
#     elif op == '*':
#         print("Result:", a * b)
#     elif op == '/':
#         print("Result:", a / b)
#     else:
#         print("Invalid operation!")

# except ZeroDivisionError:
#     print("Division by zero is not allowed.")
# except Exception as e:
#     print("Unexpected error:", e)

#====== lab - 2 ======
# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     result = a / b
#     print("Result:", result)

# except ValueError:
#     print("Please enter numbers only.")
# except ZeroDivisionError:
#     print("You cannot divide by zero.")
# except Exception:
#     print("Something went wrong.")

#======== Practical Example ==========
#====== lab - 7 ======
# try:
#     a = float(input("Enter the value a : "))
#     b = float(input("Enter the value b : "))
#     op = input("Enter operation (+, -, *, /): ")

#     if op == '+':
#         print("Result:", a + b)
#     elif op == '-':
#         print("Result:", a - b)
#     elif op == '*':
#         print("Result:", a * b)
#     elif op == '/':
#         print("Result:", a / b)
#     else:
#         print("Invalid operation!")

# except ZeroDivisionError:
#     print("Division by zero is not allowed.")
# except Exception as e:
#     print("Unexpected error:", e)

#====== lab - 8 ======
# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     result = a / b
#     print("Result:", result)

# except ValueError:
#     print("Please enter numbers only.")
# except ZeroDivisionError:
#     print("You cannot divide by zero.")
# except Exception:
#     print("Something went wrong.")

#====== lab - 9 ======
# a =""
# try:
#     a = open("study.txt",'r')
#     data = a.read()
#     print(data)
# except Exception as e:
#     print(e)
# finally:
#     if (a is not None):
#         a.close()

#====== lab - 10 ======
# class NotEligibleForLicense(Exception):
#     pass

# def checkLicenseEligibility(age):
#     if age < 18:
#         raise NotEligibleForLicense("not eligible for driving license")
#     else:
#         print("eligible for driving license")

# try:
#     checkLicenseEligibility(20)
# except NotEligibleForLicense as e:
#     print(e)


#================================================== Que - 6 ======================================================================
#====== lab - 1 ======
# class student:
#     name = 'devanshi'
#     age = 20
#     email = 'devanshi@gamil.com'

#     def person(display):
#         print("student information ")
#         print(display.name,display.age,display.email)
# s = student()
# s.person()

#======== Practical Example ==========
#====== lab - 11 ======
# class fruit:
#     name = 'mango'
#     colour = 'yellow'
#     test = 'sweet'

#     def eat(display):
#         print(display.name,display.colour,display.test)
# f = fruit()
# f.eat()

#====== lab - 12 ======
# x = 10
# class Demo:
#     def show(self):
#         y = 20
#         print("Local variable y ", y)
#         print("Global variable x ", x)
# d = Demo()
# d.show()

# print("Global variable", x)


#================================================== Que - 7 ======================================================================
#====== lab - 1 ======
# class school:
#     def information(self):
#         print("this is a school")

# class student(school):
#     def school_info(self):
#         print("this is a student")
# print("========= singel inheritance =======")
# print()
# s = student()
# s.information()
# s.school_info()
# print()

# class teacher:
#     def teach(self):
#         print("teacher teaches a subject")
# class sportsCoach:
#     def trainer(self):
#         print("training in games")
# class PTteacher(teacher,sportsCoach):
#     def role(self):
#         print("PT teche teach and training")
# print("========= multiple inheritance ==========")
# print()
# p = PTteacher()
# p.teach()
# p.trainer()
# p.role()
# print()

# class person:
#     def person_info(self):
#         print("this is a person")
# class staff(person):
#     def staff_info(self):
#         print("staff member")
# class principal(staff):
#     def principal_info(self):
#         print("school principal")
# print("======== multilevel inheritance =========")
# print()
# p = principal()
# p.person_info()
# p.staff_info()
# p.principal_info()
# print()

# class Subject:
#     def subject_info(self):
#         print("Subjects teach")

# class Math(Subject):
#     def math_info(self):
#         print("Math is calculating")

# class Science(Subject):
#     def science_info(self):
#         print("Science is difficlut")

# print("======= Hierarchical Inheritance =======")
# print()
# m = Math()
# s = Science()
# m.subject_info()
# m.math_info()
# s.subject_info()
# s.science_info()
# print()

# class School:
#     def school_info(self):
#         print("This is a school")

# class Department(School):
#     def department_info(self):
#         print("department of school")

# class Teacher:
#     def teacher_info(self):
#         print("This is a teacher")

# class ScienceTeacher(Department, Teacher):
#     def sci_teacher_info(self):
#         print("Science teacher in Science Department")

# print("=== Hybrid Inheritance ===")
# print()
# st = ScienceTeacher()
# st.school_info()
# st.department_info()
# st.teacher_info()
# st.sci_teacher_info()

#======== Practical Example ==========
#====== lab - 13 ======
# class father:
#     def father_info(self):
#         print("this is father")
# class child(father):
#     def child_info(self):
#         print("this is child")
# c = child()
# c.father_info()
# c.child_info()

#====== lab - 14 ======
# class Vehicle:
#     def Vehicle_info(self):
#         print("this is a Vehicle")
# class car(Vehicle):
#     def car_info(self):
#         print("this is a car")
# class ElectricCar(car):
#     def ElectricCar_info(self):
#         print("car use in electric battery")
# e = ElectricCar()
# e.Vehicle_info()
# e.car_info()
# e.ElectricCar_info()

#====== lab - 15 ======
# class father:
#     def skill(self):
#         print("drive")
# class mother:
#     def talent(self):
#         print("cooking")
# class child(father,mother):
#     def hobby(self):
#         print("creating new art")
# c = child()
# c.skill()
# c.talent()
# c.hobby()

#====== lab - 16 ======
# class animal:
#     def sound(self):
#         print("animal sound")

# class dog(animal):
#     def bark(self):
#         print("dogs barks")

# class cat(animal):
#     def meow(self):
#         print("cat meow")
# d = dog()
# d.sound()
# d.bark()
# c= cat()
# c.sound()
# c.meow()
    
#====== lab - 17 ======
# class a:
#     def showA(self):
#         print("class A")

# class b(a):
#     def showB(self):
#         print("class B")

# class c(a):
#     def showC(self):
#         print("class C")

# class d(b,c):
#     def showD(self):
#         print("class D")
# d = d()
# d.showA()
# d.showB()
# d.showC()
# d.showD()

#====== lab - 18 ======
# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(f"name: {self.name}")

# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age

#     def show(self):
#         super().show()
#         print(f"age: {self.age}")


# c = Child("devanshi", 20)
# c.show()


#================================================== Que - 8 ======================================================================
#====== lab - 1 ======
# class Demo:
#     def show(self, a=None, b=None):
#         if a is not None and b is not None:
#             print(a + b)
#         elif a is not None:
#             print(a)
#         else:
#             print("Nothing to show")

# d = Demo()
# d.show()        
# d.show(5)       
# d.show(5, 10)   



# class Animal:
#     def sound(self):
#         print("Animals make sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# a = Animal()
# a.sound()   

# d = Dog()
# d.sound()   

#========== Practical Example ==========
#====== lab - 19 ======
# class Example:
#     def show(self, a=None, b=None):
#         if a is not None and b is not None:
#             print("Two arguments:", a, b)
#         elif a is not None:
#             print("One argument:", a)
#         else:
#             print("No arguments")

# e = Example()

# e.show()
# e.show(10)
# e.show(10, 20)

#====== lab - 20 ======
# class A:
#     def disp(self):
#         print("A disp calling")

# class B(A):
#     def disp(self):
#         print("B disp calling")

# b = B()
# b.disp()


#================================================== Que - 9 ======================================================================
#====== lab - 1 ======
# import sqlite3

# db = sqlite3.connect("data.db")

# db.execute("create table emp(id int primary key , name varchar(50),email varchar(50))")
# db.execute("insert into emp values(3,zeel','z@gmail.com')")

# data = db.execute("select * from emp").fetchall()
# for dt in data:
#     print(dt)

#========== Practical Example ==========
#====== lab - 21 ======
# import sqlite3

# db = sqlite3.connect("data.db")

# db.execute("create table emp(id int primary key , name varchar(50),email varchar(50))")
# db.commit()

#====== lab - 22 ======
# import sqlite3

# db = sqlite3.connect("data.db")

# db.execute("create table emp(id int primary key , name varchar(50),email varchar(50))")
# db.execute("insert into emp values(3,zeel','z@gmail.com')")

# data = db.execute("select * from emp").fetchall()
# for dt in data:
#     print(dt)


#================================================== Que - 10 ======================================================================
#====== lab - 1 ======
# import re
# a = re.search('Python',"programming in Python")    
# print(a)

#====== lab - 2 ======
# a = re.match('programming',"programming in Python")
# print(a)

#========== Practical Example ==========
#====== lab - 23 ======
# k = re.search('abc$',"Hello pytHoln abc")
# print(k)

#====== lab - 24 ======
# num = input("Enter your number: ")
# k = re.match('[0-9]{5}$',num)
# if k:
#     print("Valid number")
# else:
#     print("Invalid number")




























