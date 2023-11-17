"""
    W pythonie mamy pętle for, while
"""

"""
    Mini zadanie:
    Chcemy wczytać od uzytkownika liczbe calkowita wieksza od 10. Jesli osoba poda liczbe mniejsza niz 10 to program
    ma sie nie konczyc tylko jeszcze raz poprosic o liczbe wieksza od 10
"""

x = input("Podaj liczbę całkowitą większą od 10: ")
x = int(x)
while x < 10:
    print("Podana liczba jest mniejsza od 10")
    x = input("Podaj liczbę całkowitą większą od 10: ")
    x = int(x)
print(f"Twoja liczba wieksza od 10 to {x}")

while(2 < 10):
    print("2 jest mniejsze od 10")