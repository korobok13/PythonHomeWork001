# Найдите сумму цифр трехзначного числа.

# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

a = int(input('Введите трехзначное число: '))

res = a // 100 + (a % 100) // 10 + a % 10

print((a),'->',(res),'(',a // 100,'+',(a % 100) // 10,'+',a % 10,')')