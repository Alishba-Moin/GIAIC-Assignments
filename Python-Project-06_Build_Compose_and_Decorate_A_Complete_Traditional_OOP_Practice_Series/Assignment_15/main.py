'''15. Method Resolution Order (MRO) and Diamond Inheritance
Assignment:
Create four classes:

A with a method show(),

B and C that inherit from A and override show(),

D that inherits from both B and C.

Create an object of D and call show() to observe MRO.
'''

# Create class A
class A:
    def show(self):
        return 'Message from A'  # method in class A
    
# Create class B that inherits from A and overrides show()
class B(A):
    def show(self):
        return 'Message from B'  # method in class B

# Create class C that inherits from A and overrides show()
class C(A):
    def show(self):
        return 'Message from C'  # method in class C

# Create class D that inherits from both B and C
class D(B, C):
    pass  # no need to override show(), MRO decides which method to call

# create an object of class D
d = D()

# print Method Resolution Order (MRO) for class D
print(D.mro())

# call show() method of D (MRO will determine which show() to call)
print(d.show())
