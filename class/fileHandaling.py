# f = open("test.txt",'w')                 #write
# f.write("hello python")
# f.close()

# f = open("test.txt",'r')                 #read
# data = f.read()
# print(data)

# f = open("test.txt",'a')                 #append
# f.write("\n hello python !")
# f.close()

# f = open("test.txt",'r')
# while True:
#     data = f.readline()
#     if 'java' in data:
#         print(data)
#     if not data:
#         break

# f = open("test.txt",'r')
# while True:
#     data = f.readline()
#     print(len(data))
#     if not data:
#         break

# with open ('test.txt','r')as f:
#     print(f.tell())
#     f.seek(10)
#     print(f.tell())
#     data = f.read()
#     print(f.tell())
#     print(data)

# with open('test.txt','r+') as f:
#     f.write("something....")
#     f.seek(0)
#     data = f.read()
#     print(data)

# with open('test1.txt','w+') as f:
    # f.write("something....")
    # f.seek(0)
    # data = f.read()
    # print(data)

with open("bappa.jpg",'rb') as f:
    data = f.read()
    print(data)