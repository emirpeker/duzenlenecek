class A():
    def f(self):
        print(self.g())
    def g(self):
         return 10
class B(A):
    def g(self):
        return 14
    def h(self):
        return 18
a = A ()
b = B ()
a.f()