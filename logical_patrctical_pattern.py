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

