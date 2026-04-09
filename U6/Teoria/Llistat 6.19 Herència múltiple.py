class A:
    def print_A(self):
        print("A")

class B:
    def print_B(self):
        print("B")

class C(A, B):
    def print_C(self):
        print("C")

c = C()
c.print_A()
c.print_B()
c.print_C()