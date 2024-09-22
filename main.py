num = input("Введите число, состоящее из 8 разрядов: ")
while len(num) != 8:
    num = input("Введите корректное число из 8 разрядов: ")   
sum = sum(int(i) for i in num)
print("Сумма всех цифр числа равна: ", sum)