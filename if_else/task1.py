"""
    Mini zadanie:
    Napisz program, który pobiera od uzytkownika 2 liczby, 
    dodaje je do siebie i sprawdza czy suma jest większa od 10.
    Jesli tak to wyswietla Prawda w przeciwnym razie Falsz
"""

x = input("podaj pierwszą liczbe: ")
y = input("podaj drugą liczbę: ")
x = int(x)
y = int(y)
print(f"pierwsza liczba: {x}, druga liczba: {y}")

if x+y > 10:
    print("True")
else:
    print("False")


