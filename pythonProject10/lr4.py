def pr1():
    try:
        a = input("Введите число:")
    except ZeroDivisionError:
        print("Ноль")
    except ValueError:
        print("Символ")
    else:
        if int(a) % 3 == 0:
            print("Число делится на 3")
        else:
            print("Число не делится на 3")
pr1()

def pr2():
    try:
        a = 100
        b = input("Введите число:")
        c = a // int(b)
    except ValueError:
        print("Строка")
    except ZeroDivisionError:
        print("Ноль")
    else:
        if int(b) > a:
            print(float(c))
        else:
            print("Результат:", c)
pr2()

def pr3():
    try:

        a = input("Введите день:")
        b = input("Введите месяц:")
        c = input("Введите год:")
    except ValueError:
        print("Символ")
    except ZeroDivisionError:
        print("Ноль")
    else:
        if int(a) * int(b) == int(c[2:]):

            print("Маг")
        else:
            print("Не маг")
pr3()

def pr4():
    a = input("Введите 6 цифр")
    for i in range(len(a)):
        if int(a[0]) + int(a[1]) + int(a[2])  == int(a[3]) + int(a[4]) + int(a[5]):
            print("Счастливый билет:")
            break
        else:
            print("Не счастливый")
            break
pr4()

