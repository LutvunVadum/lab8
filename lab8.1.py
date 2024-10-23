def find_divisors(num):
    divisors = [i for i in range(1, num+1) if num % i == 0]
    return divisors

numbers = [int(input(f"Введіть число {i+1}: ")) for i in range(7)]

for number in numbers:
    divisors = find_divisors(number)
    print(f"Додатні дільники числа {number}: {', '.join(map(str, divisors))}")
