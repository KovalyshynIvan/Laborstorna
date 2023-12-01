while True:

    t = input("Виберіть операцію (+;-;/;*;exit): ")

    if t == 'exit':
        print("Гарного дня!")
        break

    t1 = int(input("Введіть перше число: "))
    t2 = int(input("Введіть друге число: "))

    if t == '+':
        c = t1 + t2
    elif t == '-':
        c = t1 - t2
    elif t == '*':
        c = t1 * t2
    elif t == '/':
        if t2 == 0:
            print("Ділити на нуль не можна!")
        elif t1 == 0:
            print("Ділити на нуль не можна!")
            continue
        c = t1 / t2
    else:
        print("Помилка!")
        continue

    print("Результат : ", c)