def l1():

    password = input('Введите пароль:')
    is_numeric = False
    is_upper = False
    is_lower = False
    is_spec = False

    for char in password:
        if char.isnumeric():
            is_numeric = True
        elif char.isupper():
            is_upper = True
        elif char.islower():
            is_lower = True
        if char in "@$%^":
            is_spec = True

    if len(password) > 5 and is_numeric and is_upper and is_lower and is_spec:
        print('Пароль подходит')
        password2 = input('Введите пароль ёще раз:')
        if password == password2:
            print('Пароль принят')
        else:
            print('Пароль не подходит')
    elif len(password) <= 5:
        print('Пароль короткий')
    elif not is_numeric:
        print('Пароль не подходит, добавьте цифры')
    elif not is_upper:
        print('Пароль не подходит, добавьте верхний регистр')
    elif not is_lower:
        print('Пароль не подходит, добавьте нижний регистр')
    elif not is_spec:
        print('Пароль не подходит, добавьте спецзнаки')

def l2():

    a = int(input('Введите место в вагоне:'))
    if a not in range(1, 55):
        print('неправильный номер места')
    elif a % 2 == 0 and a in range(1, 37):
        print('Место', a, 'находится в купе сверху')
    elif a % 2 == 1 and a in range(1, 37):
        print('Место', a, 'находится в купе снизу')
    elif a % 2 == 0 and a in range(37, 55):
        print('Место', a, 'находится c боку сверху')
    elif a % 2 == 1 and a in range(37, 55):
        print('Место', a, 'находится с боку снизу')

def l3():

    a = int(input('Введите год:'))
    if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
        print('Год', a, 'високосный')
    else:
        print('Год', a, ' не високосный')

def l4():

    a = input("Введите один из трех цветов (красный, синиий, желтый):")
    b = input("Введите один из трех цветов (красный, синиий, желтый):")
    r = 'красный'
    bl = 'синий'
    y = 'желтый'
    if a == b:
        print("Цвет не изменился!")
    elif a == r and b == bl:
        print("Получился фиолетовый!")
    elif a == r and b == y:
        print("Получился оранжевый!")
    elif a == bl and b == y:
        print("Получился зеленый!")
    elif b == r and a == bl:
        print("Получился фиолетовый!")
    elif b == r and a == y:
        print("Получился оранжевый!")
    elif b == bl and a == y:
        print("Получился зеленый!")
    else:
        print("Что-то пошло не так(")

l1()