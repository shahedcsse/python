
'''class A:
    
    def m1(self):
        print("This is the methos A")

class B(A):
    def m2(self):
        print("this is method B")  
        super().m1 ()     

b=B()
b.m2()'''

# super class variable 
'''
a,b =10,20
class A:
    x,y=30,40
    def m1(self):
        print("This is the methos A")

class B(A):
    def m2(self):
        print("this is method B")  
        print(super().x+super().y) 
        print(self.x+self.y)
        print(globals()['a']+globals()['b'])

bobj=B()
bobj.m2()        '''

