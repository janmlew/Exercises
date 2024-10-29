import przykladowy_modul as pm
from przykladowy_modul import PI as pi, g as gf
from datetime import datetime, date, time


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

template = "{0:.2f} {1:s} is an equivalent of ${2:d}."
print(template.format(4.556, "Peso", 1))

val = "español"
val_utf8 = val.encode("utf-8")  # or 'latin1', 'utf-16', 'utf-16le'
print(val_utf8)
print(type(val_utf8))
print(val_utf8.decode('utf-8'))

s = '3.14159'
fval = float(s)
fval = int(fval)
print(bool(fval))
print(fval is not None)
print(type(None))

dt = datetime(2011, 10, 29, 20, 30, 21)
print(dt.day)
