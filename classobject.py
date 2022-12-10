#class of objaect
'''class MyClass:
    def func(self):
        pass
    def display(self,name):
        print("name is:",name)

mc=MyClass()
mc.func()
mc.display('shahed')'''

#decler the classs variable

'''class Myclass:
    a,b=100,300  #class variable
    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)

mc=Myclass()
mc.add()
mc.mul()'''


#  same name of local variable, gobal variable ,class variable


'''a,b=10,20   #global variable 
class Myclss:
    a,b=10,20
    def add(self,a,b):
        print(a+b)
        print (self.a+self.b)
        print (globals()['a']+globals()['b'])


mc=Myclss()
mc.add(100,320)'''

#Myclass().add(100,23) name less object

#object memory location

class Myclass:
    def m1():
        pass
c1=Myclass()
c2=Myclass()
c3=c1
print(id(c1))
print(id(c2))
print(id(c3))


