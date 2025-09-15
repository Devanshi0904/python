# st = {
#     "name":"devanshi",
#     "email":"devanshi@gmail.com",
#     "language":["guj","hindi","eng"]
# }
# print(st)
# print(st['name'])
# print(st.get('name'))

# st['name'] = "nilay"
# print(st)

# st.update({"subject":"python","stream":"IT"})
# print(st)
# print(st['language'])

s = dict(name="devanshi",email="devanshi@gmail.com")
# print(s)
# print(s['name'])
# print(s.get('name'))
# print(s.keys())
# print(s.values())
# print(s.items())

# for i in s.items():
#     print(i)

# s['name']="tisha"
# print(s)

# s.update({"name":"tisha","phone":"9157568614"})
# print(s)

# s.pop('name')
# print(s)

# s.popitem()
# print(s)

# s.clear()
# print(s)

# y=s.copy()
# print(y)

# del s
# print(s)

student = {
    "zinal0":{
        "email":"zinal@gmail.com",
        "phone":"8780610261"
    },
    "hetal":{
        "email":"hetal@gmail.com",
        "phone":"8651646461"
    }
}
# print(student)

# for i,j in student.items():
#     print(i)
#     for a , b in j.items():
#         print(a,b)


# x = ('key1','key2','key3')
# y = "hello"

# dict = dict.fromkeys(x,y)
# print(dict)


# l = [1,2,3,4,5,6]
# a = 6
# k = dict.fromkeys(l,a)
# print(k)