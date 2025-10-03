#value error                           #int aypu to char hoy to value error ave
# a = "abc"
# b = int(a)
# print(b)

#index error                           #value ma jetli amt che aena thii vadare hoy aetle range ma thai aeni error
# k = [10,20,30]       
# print(k[3])

#key error                                # jeni value api aen siuvay nu lakhe to key error ave 
# a = {"name":"devanshi"}
# print(a["email"])

#file not found                           #file nii hot save te 
# f = open("tes.txt",'r')
# data = f.read()
# print(data)

#type error                                 #varivale valid  nii apiye tyare
# c = "hello"+10
# print(c)

#name error                                 #koy name ke saku nay apiyr ne variable print karva kahiye tyare
# print(a)










#=========================================================== EXCEPTION =====================================================
print("program start")
try:  
    a = 10
    b = a/2
    print(b)
except Exception as e:
    print(e)
else:                                     #sachu hoy to hoy to print nma thay
    print("every thing is okay")
# finally:                                  #erroe hoy ke na hoy to pan excecute the inally
#     print("always executable")

print("program ended")


# f =""
# try:
#     f = open("tes.py",'r')
#     data = f.read()
#     print(data)
# except Exception as e:
#     print(e)
# finally:
#     if (f is not None):
#         f.colse()


# def test():
#     try :
#         a = int(input("enter number :"))
#         return 1
#     except Exception as e:
#         return 0
#     finally:
#         print("program executed....")
# a = test()
# print(a)
