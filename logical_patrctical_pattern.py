# *
# **
# ***
# ****
# *****
# for i in range(5):
#     print("*"*(i+1))
 

#     *
#    **
#   ***
#  ****
# *****
# for i in range(1,6):
#     print(" "*(5-i)+'*'*i)


# *****
# ****
# ***
# **
# *
# for i in range(5,0,-1):
#     print("*"*i)


# *****
#  ****
#   ***
#    **
#     *
# for i in range(5,0,-1):
#     print(" "*(5-i)+"*"*i)


#     * 
#    * * 
#   * * *
#  * * * *
# * * * * *
# for i in range(1,6):
#     print(" "*(5-i)+"* "*i)


# * * * * * 
#  * * * * 
#   * * *
#    * *
#     *
# for i in range(5,0,-1):
#     print(" "*(5-i)+"* "*i)


#     * 
#    * * 
#   *   *
#  *     *
# * * * * *
# n = 5

# for i in range(1, n + 1):
#     print(" " * (n - i), end="") 

#     for j in range(1, i + 1):
#         if j == 1 or j == i or i == n:
#             print("* ", end="")
#         else:
#             print("  ", end="")  

#     print()


#           * 
#         * * * 
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
# for i in range(5):
#     for k in range(5-i):
#         print(" ",end=" ")

#     for j in range((i*2)+1):
#         print("*",end=" ")
#     print()


#           * 
#         *   * 
#       *       *
#     *           *
#   * * * * * * * * *
# for i in range(5):
#     for k in range(5-i):
#         print(" ",end=" ")
#     for j in range((i*2)+1):
#         if  j==0 or j==(2*i) or i==4:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


#     * 
#    * * 
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# for i in range(1,5):
#     print(" "*(5-i)+"* "*i)
# for j in range(5,0,-1):
#     print(" "*(5-j)+"* "*j)


#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *
# for i in range(1, 6):
#     print(" " * (5 - i), end="") 

#     for j in range(1, 2*i):
#         if j == 1 or j == 2*i - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")  

#     print()
# for i in range(4,0,-1):
#     print(" " * (5 - i), end="") 

#     for j in range(1, 2*i):
#         if j == 1 or j == 2*i - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")  

#     print()


# *
# **
# ***
# ****
# *****
# ******
# *****
# ****
# ***
# **
# *
# for i in range(6):
#     print("*"*(i+1))
# for i in range(5,0,-1):
#     print("*"*i)





# ====================================================== number/alphbet pattern ==========================================================

# 1
# 12
# 123
# 1234
# 12345
# for i in range(5):
#     for j in range(i+1):
#         print(j+1,end="")
#     print()


# 12345
# 1234
# 123
# 12
# 1
# for i in range(5,0,-1):
#     for j in range(i):
#         print(j+1,end="")
#     print()


# 0
# 10
# 010
# 1010
# 01010
# for i in range(6):
#     for j in range(1,i+1):
#         print((j+i)%2,end="")
#     print()


# 1
# 01
# 101
# 0101
# 10101
# for i in range(6):
#     for j in range(i):
#         print((j-i)%2,end="")
#     print()


# 1
# 22
# 333
# 4444
# 55555
# for i in range(6):
#     for j in range(i):
#         print(i,end="")
#     print()


# 55555
# 4444
# 333
# 22
# 1
# for i in range(5,0,-1):
#     for j in range(i):
#         print(i,end="")
#     print()


# 1
# 23
# 456
# 78910
# num=1
# for i in range(5):
#     for j in range(i):
#         print(num,end="")
#         num+=1
#     print()


#     1 
#    1 2 
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5
# n = 5
# for i in range(1, n+1):
#     print(" "*(n-i), end="")
#     for j in range(i):
#         print(j+1, end=" ")
#     print()


# 1 2 3 4 5 
#  1 2 3 4 
#   1 2 3
#    1 2
#     1
# n=5
# for i in range(n,0,-1):
#     print(" "*(n-i), end="")
#     for j in range(i):
#         print(j+1, end=" ")
#     print()


# 1
# 21
# 321     
# 4321
# 54321
# for i in range(6):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print() 


# A
# AB
# ABC
# ABCD
# ABCDE
# for i in range(5):
#     for j in range(i+1):
#         print(chr(65+j),end="")
#     print()


# ABCDE
# ABCD
# ABC
# AB
# A
# for i in range(5,0,-1):
#     for j in range(i):
#         print(chr(65+j),end="")
#     print()


# A
# BB
# CCC
# DDDD
# EEEEE
# for i in range(5):
#     for j in range(i+1):
#         print(chr(65+i),end="")
#     print()


# EEEEE
# DDDD
# CCC
# BB
# A
# for i in range(5,0,-1):
#     for j in range(i):
#         print(chr(64+i),end="")
#     print()


# A
# BC
# DEF
# GHIJ
# KLMNO
# ch=65
# for i in range(6):
#     for j in range(i):
#         print(chr(ch),end="")
#         ch+=1
#     print()


#     A 
#    A B 
#   A B C 
#  A B C D 
# A B C D E 
# n = 5
# for i in range(1,n+1):
#     print(" "*(n-i),end="")
#     for j in range(i):
#         print(chr(65+j),end=" ")
#     print()


# A B C D E 
#  A B C D 
#   A B C
#    A B
#     A
# n=5
# for i in range(n,0,-1):
#     print(" "*(n-i),end="")
#     for j in range(i):
#         print(chr(65+j),end=" ")
#     print()
