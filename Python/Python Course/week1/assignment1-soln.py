def q1():
    n = int(input())
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    print(rev)


def q2():
    x1 = int(input("x1 : "))
    x2 = int(input("x2 : "))
    y1 = int(input("y1 : "))
    y2 = int(input("y2 : "))
    print(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)


def q3():
    print("X\tY\tX**Y")
    for i in range(2, 6):
        print(f"{10}\t{i}\t{10 ** i}")


def q4():
    print("1\n1\t2\n1\t2\t3\n1\t2\t3\t4")


def q5():
    print("\t\tA\t\t")
    print("\tA\t\tA\t")
    print("A\t\t\t\tA")


def q6():
    p = int(input("Enter p :"))
    n = int(input("Enter n :"))
    r = int(input("Enter r :"))
    print(f"SI : {p * n * r / 100}")


def q7():
    print(f"Wright in grams : {int(input('Weight in kg : ')) * 100}")


def q8():
    print(f"Tempearture in Celcius : {((float(input('Enter temperature in Farenheit : '))) - 32) * 5 / 9}")


def q9():
    cp = eval(input("Enter CP : "))
    sp = eval(input("Enter SP : "))
    print(f"Profit : {sp - cp}")


def q10():
    n = int(input("Enter Num : "))
    print(f"x**0.5  : {n ** 0.5}")
    print(f"x**2    : {n ** 2}")
    print(f"x**3    : {n ** 3}")
