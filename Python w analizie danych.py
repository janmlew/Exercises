import przykladowy_modul as pm
from przykladowy_modul import PI as pi, g as gf


def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False


print(isiterable('a string'))

result = pm.f(5)
# pi = pm.PI

r1 = pm.f(pi)
r2 = gf(6, pi)

print(pi is pi)
print(pi is not pi)

a = [1, 2, 3]
b = a
c = list(a)
print(a is b)
print(a is not c)
print(a == c)
a = None
print(a is None)
