

choice ="y"
while choice != "n" :

        marks = int(input("enter the marks "))
        print(marks)

        if marks >= 91 and marks <= 100:
            print(" grade a ")
        elif marks >= 71 and marks <= 90:
            print("grade b ")
        elif marks >= 51 and marks <= 70:
            print("grade c ")
        elif marks >= 35 and marks <= 50:
            print("grade d ")
        elif marks >= 0 and marks <= 35:
            print("grade f ")
        else:
             print(" invalid input if out of range (0-100) ")

        choice = input("Do you want to continue (y/n)")
