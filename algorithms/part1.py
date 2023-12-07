"""
    Napisz funkcję, która sprawdza czy liczba jest doskonała.
    Funkcja przyjmuje jeden argument o nazwie x i zwraca wartość Bool (True or False).
    Liczba naturalna n jest liczbą doskonałą, jeśli jest sumą wszystkich swoich dzielników właściwych
"""

def czy_liczba_jest_doskonala(x):
    suma_dzielnikow = 0
    i = 1
    while i < x:
        if x % i == 0:
            suma_dzielnikow = suma_dzielnikow + i
        i = i + 1
    if suma_dzielnikow == x:
        return True
    else:
        return False
    



# print(czy_liczba_jest_doskonala(6))

"""
Napisz funkcję, która sprawdza czy podana liczba jest parzysta.
Funkcja jako argument przyjmuje x i zwraca wartość Bool (True or False)
"""
def czy_liczba_jest_parzysta(x):
    if x % 2 == 0:
        return True
    else:
        return False


"""
    Napisz funkcję, która wylicza silnię z danej liczby.
    Silnia to jest: 5! = 1*2*3*4*5
    Funkcja przyjmuje jako argument x i zwraca wartość x!
"""


def silnia(x):
    wartosc = 1
    for element in range(1, x+1):
        print(f"obieg petli numer {element}. Wykonuje przypisuje zmiennej wartosc={wartosc}*{element}")
        wartosc = wartosc*element
    return wartosc


"""
    Napisz funkcję, która dla danej liczby i potęgi zwróci wartość.
    Funkcja przyjmuje argument n oraz k i zwraca n^k.
"""

def potega(n, k):
    wartosc = 1
    for element in range(1, k+1):
        wartosc = wartosc*n
    return wartosc


print(potega(2,4))

"""
    Ciag Fibonacciego to ciag ktorego dwa pierwsze elementy to 1 i 1 a kolejne powstaja poprzez zsumowanie dwoch poprzednich.
    1 1 2 3 5 8 13 21 34 55 ...
    Napisz funkcje, ktora wylicza n-ty wyraz ciagu Fibonacciego.
    Jako argument przyjmuje n, zwraca n-ty wyraz ciagu Fibonacciego.
"""


def fib(n):
    ostatnia = 1 
    przedostatnia = 1 
    if n < 3:
        return 1
    for el in range(3, n+1):
        biezacy = ostatnia + przedostatnia
        ostatnia = przedostatnia
        przedostatnia = biezacy
    return przedostatnia

print(fib(7))