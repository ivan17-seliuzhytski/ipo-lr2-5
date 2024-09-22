num = input("Введите число, состоящее из 8 разрядов: ")
if len(num) == 8:
    sum = sum(int(i) for i in num)
    print("Сумма всех цифр числа равна: ", sum)
else:
    num = input("Введите корректное число из 8 разрядов: ")