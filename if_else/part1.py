"""
    Mini zadanie:
    Chcemy pobrać od uzytkownika jakąś liczbę.
    Jeśli liczba ta jest większa od parzysta to wyświetlamy na konsoli LICZBA JEST PARZYSTA
    w przeciwnym przypadku wyświetlamy LICZBA JEST NIEPARZYSTA
"""


user_input = input("PODAJ LICZBĘ CAŁKOWITĄ: ")
user_input = int(user_input)
print(f"LICZBA PODANA PRZEZ UŻYTKOWNIKA TO {user_input} A JEJ TYP TO {type(user_input)}")

# Operator modulo czyli reszta z dzielenia %

# Instrukcja warunkowa

def check_modulo(x):
    if x % 2 == 0:
        print("LICZBA JEST PARZYSTA")
    else:
        print("LICZBA JEST NIEPARZYSTA")


check_modulo(user_input)