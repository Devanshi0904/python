# print("=========== squre ==========")
# for j in range(5):
#         print("*"*5)


# for i in range(5):
#     for j in range(i+1):
#         print("*",end="")
#     print()


# print("============= left up ===========")

# for i in range(5):
#     print("*"*(i+1))

# print("============ left down ============")

# for i in range (5,0,-1):
#     print("*"*i)

# print("==========right down ==========")

# for i in range (5,0,-1):
#     print(' '*(5-i)+'*'*i)

# print("============ right up =========")

# for i in range (1,6):
#     print(' '*(5-i)+'*'*i)


# print("============ up tectangel ============")
# for i in range (1,6):
#     print(' '*(5-i)+'* '*i)


# print("======== down tectengel ==============")
# for i in range (5,0,-1):
#     print(' '*(5-i)+'* '*i)




# print("========= odd num triangel ======== ")
# for i in range (5):
#     for k in range (5-i):
#       print(" ",end=" ")
#     for j in range ((i*2)+1): 
#       print("*",end=" ")
#     print()



# print("========= dimond ===========")
# for i in range (5):
#     print(' '*(5-i),'* '*(i+1))
# for i in range (4,0,-1):
#     print(' '*(4-i+2),'* '*i)


# print("============ hollow dimond ===========")


# for i in range(5):     #i=1,2,3,4,5
#     for j in range( 5 - i ):    #4,3,2,1,0 space
#         print(" ", end="")
#     for k in range(i+1):     
#         if k == 0 or k == (i):
#             print("* ",end="")
#         else:
#             print("  ", end="")  
#     print()
# for i in range(4, 0, -1):     #i=4,3,2,1
#     for j in range( 4 - i + 2):
#         print(" ", end="")
#     for k in range(i):
#         if k == 0 or k== (i - 1): 
#             print("* ", end="")
#         else:
#             print("  ", end="") 
#     print()


# print("======== 1,12,123,1234..... left up =========")

# for i in range(5):
#     for j in range(i+1):
#         print(j+1,end="")
#     print()


# print("========= 1,2,3,4,.....left up ========== ")
# num=1
# for i in range(5):
#     for j in range(i+1):
#         print(j,end="")
#         num += 1
#     print()

#// or

# for i in range(1,6):
#     for j in range(i):
#         print((i*(i-1))//2 + 1 + j,end="")
#     print()


# print("=========== 5,54,543,5432,....========")

# for i in range (5,0,-1):
#     for j in range(i,6):
#         print(j,end=" ")
#     print()


# print("======== 0,10,010,1010,..... ===========")

# for i in range (1,6):
#     for j in range(1,i+1):
#         print((j+i)%2,end=" ")
#     print()


# print("========= 1,01,101,0101,..... ========")
# for i in range (1,6):
#     for j in range(0,i):
#         print((j-i)%2,end=" ")
#     print()


# print("========== t * pattern ===========")

# print("*"*5)
# for i in range (1,4):
#     print(" ","*")


# print("========= H * pattern ==========")

# for i in range(5):
#     for j in range(5):
#             if j==0 or j==4 or i==5//2:
#                 print("* ",end="")
#             else:
#                 print("  ",end="")
#     print()




# print("=========== abcd.... left up =========")

# char='A'
# for i in range(1,6):
#     for j in range(i):
#         print(char,end="")
#         char =  chr(ord(char)+1)
#     print()



 
print("========= damru ==========")

lines = 10
for i in range(1,lines+1):
    for j in range(1,lines+1):
        if j==1 or j==lines or j==i or j==lines+1-i:
            print("*",end="")
        else :
            print(" ",end="")
    print()




# print("=========== tir ===========")
# for i in range (5):
#     print("*",end="")
#     print(" ",end="")
# for i in range (5):
#     print("*",end="")
    




# print("========== * temple =========")
# for i in range(4):     
#     for j in range( 4 - i ):    
#         print(" ", end="")
#     for k in range(i+1):     
#         if k == 0 or k == (i):
#             print("* ",end="")
#         else:
#             print("  ", end="") 
#     print()
# for i in range(3):
#     print(" *"*4)