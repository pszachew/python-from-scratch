book = {
    'author': 'Wyspianski',
    'title': 'Wesele',
    'year': 1964,
    'country': 'Poland'
}

book['author'] = 'Konopnicka' # zmiana w wartości pola autor


print("Zawartosc slownika")
for key in book.keys():
    print(f"{key}:{book[key]}")