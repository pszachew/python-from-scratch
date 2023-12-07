
ksiazka = {
    'autor': 'Konopnicka',
    'tytul': 'Wesele',
    'strony': 300,
    'recenzje': [5, 2, 3, 4, 1]
    }

def print_dictionary(x):
    print("ZAWARTOSC SLOWNIKA")
    for key in x.keys():
        print(f"{key}:{x[key]}")

    
def edycja_danych(x):
    print("ktore pole chcesz edytowac")
    pole = input()
    if pole in x.keys():
        print("podaj wartosc")
        wartosc = input()
        x[pole] = wartosc
    else:
        print(f"Klucz {pole} nie istnieje w naszym slowniku")

def srednia_recenzji(x):
    recenzje = x['recenzje']
    srednia = sum(recenzje)/len(recenzje)
    print(f"srednia z recenzji to {srednia}")

while True:
    print("==="*20)
    print('Co chcesz zrobic?')
    print('e - exit')
    print('d - wyswietl slownik')
    print('ed - edytuj dane')
    print('r - recenzja')
    user_input = input()
    if user_input == 'e':
        break
    if user_input == 'd':
        print_dictionary(ksiazka)
    if user_input == 'ed':
        edycja_danych(ksiazka)
    if user_input == 'r':
        srednia_recenzji(ksiazka)

