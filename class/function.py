# def hello():
#     print("hello")
# hello()

# def square(a):
#     print(a*a)
# square(10)

# def add(a,b):
#     print(a+b)
# add(10,20)



# def add (a,b):
#     return a+b
# k = add(10,20)
# print(k)

# def square(a):
#     return a*a
# j = square(10)
# print(j)



# def person (id=0,name="xyz",email="dv@gmail.com"):
#     print(id, name, email)
# person(name="devanshi",email= "devanshi@gmail.com")


#============ arbitary argument ====================
 
# def add (*a):
#     print(a)
# add(10,20,30,40,50,60)

# def person(**a):
#     print(a)
# person(name="zinal",email="zinal@gmail.com")


#=============== lamda function ============

# a = lambda a,b : a+b
# print(a(10,20))

# b = lambda a :a*a
# print(b(50))







#===================================================== SCOPE =======================================================

# a=10

# def test():
#     global a
#     a = 50
#     print("test : ",a)
# print(a)
# test()
# print(a)






#==================================================== RECURSION =====================================================
# def square(a):
#     print(a*a)
#     a+=1
#     if a<10:
#         square(a)
# square(2)







#================================================ MAP ==============================================
# def square (a):
#     return a*a


# l = [10,20,30,40,50,60]
# s = map(square,l)
# s = map(lambda a : a*a,l)
# print(list(s))

# ======= OR ==========

# s = []
# for i in l:
#     k = square(i)
#     s.append(k)
# print(s)




#==================================== FILTER =========================================
# l = [1,2,3,4,5,6,7,8,9]
# def evennumber (a):
#     if a%2!=0:
#         return True
#     else:
#         return False
    
# s = []
# for i in l:
#     k = oddnumber(i)
#     if k:
#         s.append(i)
# print(s)


# s = filter(oddnumber,l)
# s = filter(lambda a : a%2!=0,l)
# print(list(s))


# s = filter(evennumber,l)
# s = filter(lambda a : a%2==0,l)
# print(list(s))


#=========================== REDUCE  ==========================
# from functools import reduce
# l = [1,2,3,14,-1,5,6,17,8,9]
# def avg(a,b):
#     if a>b:
#         return a
#     else:
#         return b


# k = reduce(sum,l)
# k = reduce(lambda a,b:a+b,l)
# print(k)

# k = reduce(max,l)
# k = reduce(lambda a,b: a if a>b else b,l)
# print(k)


# k = reduce(min,l)
# k = reduce(lambda a,b : a if a<b else b,l)
# print(k)


# l = [1,2,3,4,5,6,7,8,9]
# def avg(a,b):
#     print(a,b)
# sum = reduce(lambda a, b: a + b, l)
# avg = sum / len(l)
# print(f"avg : {avg}")


# import math
# l = [1,2,3,4,5,6,7,8,9]
# def check_p_square(a):
#     if math.sqrt(a).is_integer():
#         return a
# k = filter(check_p_square,l)
# print(list(k))

#====== lamda fun OR =========

# def check_p_square(a):
#     if math.sqrt(a).is_integer():
#         return a
# k = filter(lambda a :math.sqrt(a).is_integer(), l)
# print(list(k))






#=================================================== GENRATER AND ITRATER ====================================================
# def square (a):
#     for i in range(1,a+1):
#         yield i*i
# a = iter(square(5))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))





l = ["tisha","devanshi","zeel","dhruvin","sunil"]
k = map(lambda a :"hello :"+a ,l)
print(list(k))