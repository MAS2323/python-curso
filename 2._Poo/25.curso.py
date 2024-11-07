# MRO Method Resolution Order
class A:
    def hablar(self):
        print('Hola desde A')


class B(A):
    def hablar(self):
        print('Hola desde B')


class C(A):
    def hablar(self):
        print('Hola desde C')


class F:
    def hablar(self):
        print('Hola desde F')


class D(F, C):
    pass


d = D()

d.hablar()
print(D.mro())
