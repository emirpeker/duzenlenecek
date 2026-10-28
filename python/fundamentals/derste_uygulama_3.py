class A():
    x=3
    y=5
    def f(self):
        return self.g()
    def g(self):
        return 10

class B(A):
    y=4
    z=42
    def g(self):
        return 14

    def h(self):
        return 18

a = A ()
b = B ()
print(b.x)
print(a.z)