n1 = int(input("Введіть перше число: "))
n2 = int(input("Введіть друге число: "))
n3 = int(input("Введіть третє число: "))

numbers = [n1, n2, n3]

numbers.sort(reverse=True)

for number in numbers:
    print(number)
