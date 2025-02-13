class A:
    def method(self):
        print("Method in class A")

class B(A):
    def method(self):
        print("Method in class B")

class C(A):
    def method(self):
        print("Method in class C")

class D(B, C):
    pass

class E(B, C):
    def method(self):
        print("Method in class E")

class F(C,B):
    pass

class G(D,A):
    pass

class H(A):
    pass

class J(H, C):
    pass

# Create an instance of class D
obj = D()
obj.method()
print(D.mro())
obj2 = F()
obj2.method()
print(F.mro())
obj1 = E()
obj1.method()
obj3 = G()
obj3.method()
obj4 = J()
obj4.method()