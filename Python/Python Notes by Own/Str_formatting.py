# str.format() ::

print("str.format() ::\n")
x = '{0} institute , rajkot , INDIA'
print(x.format('darshan'))
x = '{0} institute , {1} , {2}' 
print(x.format('darshan','rajkot','INDIA'))
x = '{0} institute , {1} , {2} , welcome to {0}' 
print(x.format('darshan','rajkot','INDIA'))
x = '{{{0}}} institute'
print(x.format('darshan'))
x = 'the price for {0} is ${1}'
print(x.format('iwatch','15\n'))

# String value formatting ::

print("String value formatting ::\n")
x = '{0} institute of engineering'
print(x.format('darshan')) #default formatting
x = '{0:25} institute of engineering'
print(x.format('darshan')) #minimum width
x = '{0:>25} institute of engineering'
print(x.format('darshan')) #right align , minimum width
x = '{0:^25} institute of engineering'
print(x.format('darshan')) #center align , minimum width
x = '{0:*^25} institute of engineering'
print(x.format('darshan')) #fill center align , minimum width
x = '{0:.3} institute of engineering\n'
print(x.format('darshan')) #maximum width of 3

# integer values formatting ::

print("integer values formatting ::\n")
x = 'amount = {0}' 
print(x.format(123456)) #default formatting
x1 = 'amount = {0:0=10}' # 0 fill , minimum width 12 (technique 1)
print(x1.format(123456))
x2 = 'amount = {0:010}' # 0 pad , minimum width 12 (technique 2)
print(x2.format(123456))
x = 'amount = {0: }' # space or - sign
print(x.format(123456))
print(x.format(-123456))
x = 'amount = {0:+}' # force sign
print(x.format(123456))
print(x.format(-123456))
x1 = '{0:b} {0:o} {0:x} {0:X}'
x2 = '{0:#b} {0:#o} {0:#x} {0:#X}\n'
print(x1.format(12))
print(x2.format(12))

# Decimal values formatting ::

print("Decimal values formatting ::\n")
x = 'amount = {0}' # default formatting
print(x.format(12.3456789))
x1 = 'amount = {0:10.2e}' # exponential formatting with two precession
x2 = 'amount = {0:10.2f}' # floating formatting with two precession
print(x1.format(12345.6789))
print(x2.format(12345.6789))