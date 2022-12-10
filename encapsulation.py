
#privet variable within class 

'''class myClass:
    __a=100

    def dis(self):
        print(self.__a)

obj=myClass()
obj.dis()'''

#privet method access with in a methode

class myclass:
    def __disp1(self):    #this private method
        print ("this is a display 1 method")

    def disp2(self):
        print("this is a display 2 method")   
        self.__disp1()

obj=myclass()
#obj.__disp1()
obj.disp2()
