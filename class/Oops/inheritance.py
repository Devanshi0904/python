# class clg :
#     def __init__(self,id,name,email):
#         self.id = id
#         self.name = name
#         self.email = email
    
#     def display(self):
#         print(self.id,self.name,self.email)

# class student(clg):
#     def __init__(self, id, name, email):
#         super().__init__(id, name, email)

# c = clg
# c.display(10,"devanshi","devanshi@gmail.com")
# # c.__init__()









# class animal():

#     def __init__(self,name):
#         self.name = name

#     def seelp(self):
#         print("animal is sleeping")  
    
#     def eat(self):
#         print("animal is eating ")
    
# class dog(animal):

#     def __init__(self, name,breed):
#         super().__init__(name)
#         self.breed = breed

#     def bark(self):
#         print(f"the dog {self.name} of breed {self.breed} is barking")

# d = dog("tommy","german shepherd")
# d.bark()
# d.seelp()
# d.eat()




#============================================================ access moditify i. public  ,  ii.privet_   , iii.protected___ ====================

# class demo :

#     __name = "XYZ"
#     email = "xyz@gmail.com"

#     def show(self):
#         print(self.__name,self.email)

# d = demo()
# print(dir(d))
# d.__name = "ABC"
# d.show()