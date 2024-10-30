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
print(dt.day)  # dt.minute
print(dt.date())
print(dt.time())
print(dt.strftime('%m/%d/%Y %H:%M'))
print(dt.strptime('20091031', '%Y%m%d'))
'''
%Y - yyyy
%y - yy
%m - mm [0, 11]
%d - dd
%H - 24h
%I - 12h
%M - mm [0, 59]
%S - ss [0, 61] where 60 & 61 represent jump (?)
%w - w [0, 6] where 0 = Sunday & 6 = Saturday
%U - ww [00, 53] Sunday is the first day of the week, days before it are in week 0 
%W - ww [00, 53] Monday is the first day of the week, days before it are in week 0
%z - UTC time zone shift +HHMM or -HHMM; empty = default
%F - %Y-%m-%d (e.g. 2012-4-18)
%D - %m/%d/%y (e.g. 04/18/12) 
'''
print(dt.replace(minute=0, second=0))
