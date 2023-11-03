cat = int(input("Введіть кількість кошачих років: "))

h_years = 0

if cat == 1:
    h_years = 15
elif cat >= 2:
    h_years = 15 + (cat - 1) * 9
print(f"Вік кота в людських роках: {h_years}")