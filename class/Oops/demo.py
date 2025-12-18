# =========================================== class & object ==========================================
# class pen:
#     price = 10
#     company = 'cello'
#     color = 'blue'

#     def to_write(self):
#         print("erite method calling ...")
#         print(self.price,self.company,self.color)
# p = pen()
# p.to_write()

# class student:
#     name = 'devanshi'
#     age = 20
#     email = 'devanshi@gamil.com'

#     def person(display):
#         print("student information ")
#         print(display.name,display.age,display.email)
# s = student()
# s.person()





#==================================== constractor ======================================
# class student:
#     def __init__(self,id,name,email):
#         self.name = name
#         self.email = email
#         self.id = id

#     def display(self):
#         print("running dispal...")
#         print(self.name,self.email,self.id)

# s = student(10,'devanshi','devu@gmail.com')
# s.display()

# s1 = student(11,'tisha','tisha@gmail.com')
# s1.display()






# class Student:

#     clg = 'DRSTC'
#     def __init__(self,id,name,email):
#         self.name  = name
#         self.email = email
#         self.id = id

#     def display(self):
#         print("Runing display...")
#         print(self.id,self.name,self.email,self.clg)

#     @classmethod
#     def sample(self):
#         print(self.clg)
#         print("Sample calling")

#     @staticmethod
#     def run():
#         print("Run calling")

# Student.clg='ABC'
# Student.sample()

# Student.run("abc")

# s  = Student(10,"sunil",'sunil@gmail.com')
# s.display()

# s1 = Student(11,"Jenil","jenil@gmail.com")
# s1.display()









# class demo:
#     id = 10
#     def disp(self):
#         print("dispaly calling")
    
#     @classmethod
#     def sample (self):
#         print("simple calling ...",self.id)

#     @staticmethod
#     def until (self):
#         print("static calling")

# d = demo()
# demo()
# d.sample()
# d.until()










class product :
    def __init__(self,id,name,price):
        self.id = id
        self.name = name
        self.price = price

    def display(self):
        print(self.id,self.name,self.price)

p = product(1,'leptop','20000')
p1 = product(2,'AC','100000')
p2 = product(3,'mobile','30000')
p.display()
p1.display()
p2.display()
