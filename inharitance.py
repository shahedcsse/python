class A:
    def m1(self):
        print("this isthe  from class A")

class B(A):
    def m2(self):
        print ("this is the class B")


aobj=A()
aobj.m1()

bobj=B()
bobj.m1()
bobj.m2()

#single inharitance 

class A:
    x,y=10,29
    def m1(self):
        print (self.x+self.y )

class B(A):
    a,b=100,299
    def m2(self):
        print (self.a+self.b)


b=B()
b.m1()               
b.m2()

#multilevel inharitance 


class A:
    x,y=10,29
    def m1(self):
        print (self.x+self.y )

class B(A):
    a,b=100,299
    def m2(self):
        print (self.a+self.b)
class C(B):
    i,j=10,99
    def m3(self):
        print (self.i+self.j)


c=C()
c.m1()
c.m2()
c.m3()

#hierarchical inharitance


