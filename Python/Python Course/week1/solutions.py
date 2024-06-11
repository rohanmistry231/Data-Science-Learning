def q1():
    print("welcome to python programming lab")
    return 0

def q2():
    print("This is a sentence with 'single quotes'")
    print('This is a sentence with "Double Quotes"')
    print('This is a sentence with """Triple Quotes"""')
    return 0

def q3():
    addr = input("Enter address")
    print(addr.replace(" ", "\n"))
    return 0

def q4():
    print(f"Greetings !!! {input('First name: ')} {input('Last name: ')}")
    
def q5():
    print(f"Hello {input('First name: ')} {input('Last name: ')}. Welcome to Python")

def q6():
    print(f"{input('First name: ')[::-1]} {input('Last name: ')[::-1]}")

def q7():
    a = 10
    b=10.0
    c=10+10j
    d="10"
    for i in [a,b,c,d]:
        print(f"{i} : {type(i)}")

def q8():
    a=input("enter val 1: ")
    b=input("enter val 2: ")
    a,b = b,a
    print(f"a : {a}\nb : {b}")

def q9():
    from math import log
    w,h,d=17,12.0,'.'
    print(f"w/2 \t\t: {w/2} , \t\tdtype : {type(w/2)}")
    print(f"w/2.0 \t\t: {w/2.0} , \t\tdtype : {type(w/2.0)}")
    print(f"h/34.1+25\t: {h/34.1+25} , \tdtype : {type(h/34.1+25)}")
    print(f"d*5 \t\t: {d*5} , \t\tdtype : {type(d*5)}")
    print(f"w//5 \t\t: {w//5} , \t\t\tdtype : {type(w//5)}")
    print(f"w%5 \t\t: {w%5} , \t\t\tdtype : {type(w%5)}")
    print(f"w**2 \t\t: {w**2} , \t\tdtype : {type(w**2)}")
    print(f"w^2 \t\t: {w^2} , \t\t\tdtype : {type(w^2)}")
    print(f"log(w) \t\t: {log(w)} , \tdtype : {type(log(w))}")

def q10():
    print(f"Volume : {4/3 * 3.14 * eval(input('Enter Radius of Sphere: '))**3}")

def q11():
    c = 24.95
    d=40/100
    tot = 0
    for i in range(1,61):
        tot += c*d
        if(i<=3):
            tot += 3
        else:
            tot += 0.75
    print(f"Total Cost : {tot}")

def q12():
    print(f"Time At End: 7:{((8.15*2 + 7.12*12)%60 + 52)%60}")

def q13():
    print(f"Minutes in 42 minutes and 42 seconds : {42 + 42/60}")
    print(f"Miles in 10 Kilometers : {10*1.6}")
    print(f"Speed in Miles per Minute : {10*1.6/(42 + 42/60)}")
    print(f"Speed in Miles per Second : {10*1.6/(42*60 + 42)}")

def q14():
    var = input("Enter your variable")
    print(f"Variable as string \t: {var, type(var)}")
    print(f"Variable as int \t: {int(var), type(int(var))}")
    print(f"Variable as float \t: {float(var), type(float(var))}")
    print(f"Variable as complex \t: {complex(var), type(complex(var))}")

def q15():
    print(f"Converted int to float value : {float(input('Enter int: '))}")

def q16():
    print(f"Converted float to int value : {round(float((input('Enter float: '))))}")

def q17():
    print(f"Sum of A and B : {float(input('Enter a : '))+float(input('Enter b : '))}")

def q18():
    print(f"Sum of A and B : {int((float(input('Enter a : '))+float(input('Enter b : '))))}")

def q19():
    print(f"Digit at ones place : {int(input('Enter num : '))%10}")

def q20():
    print(f"Tempearture in Celcius : {((float(input('Enter temperature in Farenheit : ')))-32) * 5/9}")

def q21():
    a = int(input('Enter a : '))
    b = int(input('Enter b : '))
    temp = a
    a = b
    b = temp
    print(f"a : {a} , b : {b}")

def q22():
    o = int(input("No. of 1 re coins : "))
    t = int(input("No. of 2 rs coins : "))
    f = int(input("No. of 5 rs coins : "))
    te = int(input("No. of 10 rs coins : "))
    print(f"Total : {o+t*2+f*5+te*10}")

def q23():
    a = input("Enter str1 : ")
    b = input("Enter str2 : ")
    print(f"a+b : {a+b}")
    print(f"(a+b)*5 : {(a+b)*5}")

def q24():
    x = 250+130-70
    y = (32+5.2-3)*10
    z = 100%(45//2)
    a = (40+20)*30/10
    b = ((40+20)*30)/10
    c = (40+20)*(30/10)
    d = 40+(2020)/10
    e = 40+((2930)/10)
    f = 40+(20*30/10)

    print("Solutions for given expressions")
    print("""
    x = 250+130-70
    y = (32+5.2-3)*10
    z = 100%(45//2)
    a = (40+20)*30/10
    b = ((40+20)*30)/10
    c = (40+20)*(30/10)
    d = 40+(2020)/10
    e = 40+((2930)/10)
    f = 40+(20*30/10)
    """)
    
    for i in [x,y,z,a,b,c,d,e,f]:
        print(f"{i}")



if __name__ == '__main__':
    j = [q1(), q2(), q3(), q4(),q5(),q6(),q7(),q8(),q9(),q10(),q11(),q12(),q13(),q14(),q15(),q16(),q17(),q18(),q19(),q20(),q21(), q22(),q23(),q24()]

    ch = input("Do you want to run all ? ")
    if ch == 'y':
        for i in j:
            i
            print("="*20)
