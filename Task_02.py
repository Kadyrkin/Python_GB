
# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input('Введите целое число '))
sum = 0
while number != 0:
    sum = sum + number % 10
    number = number // 10
print(f'Сумма цифр введенного числа равна {sum}')