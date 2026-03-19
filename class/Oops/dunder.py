# class demo:
#     id = 10
#     name = "devanshi0"
#     def __str__(self):
#         return f"my name is {self.name} and id is {self.id}"

# d =demo()
# print(d)

# class calc:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def __add__(self,obj):
#         return self.a+obj.a , self.b+obj.b
    
# c = calc(10,20)
# c1 = calc(30,40)

# k = c+c1
# print(k)






# class demo:
#     id = 10
#     name = "devanshi"
#     def __str__(self):
#         return f"my name is {self.name} and id is {self.id}"

# d =demo()
# print(d)

# class calc:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def __mul__(self,obj):
#         return self.a*obj.a , self.b*obj.b
    
# a = calc(50,60)
# a1 = calc(30,80)

# k = a*a1
# print(k)




#===== git copilet ,, 





#==================================================================================================================





# class demo :
#     def __init__(self,item):
#         self.item = item

#     def __setitem__(self,index,value):
#         self.index = index
#         self.value = value

#     def __getitem__(self,index):
#         return self.item[index]
    
# d = demo([10,20,30,40,50])
# d[2] = 100
# print(d[1])
    