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

# Numerical data types
ival = 17239871
print(ival**6)

fval = 7.243
fval2 = 6.78e-5
print(fval2)
print(3/2)
print(3//2)

# Strings
a = 'one method of defining string'
b = "another method"
c = """
This is a long string of characters,
one which consists of several lines.
"""
print(c.count('\n'))
print(a[10])
b = a.replace("string", "a longer string")
print(b)

a = 5.6
s = str(a)
print(list(s))
print('12\\34')
print(r'text\text\text\text')  # r = raw text
print('first part ' + 'second part')


