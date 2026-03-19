class Student:
    __name="abc"
    email = "abc@gmail.com"

    def setdata(self,name):
        self.__name=name

    def show(self):
        print(self.__name,self.email)


s = Student()
s.setdata("Tisha")
s.show()