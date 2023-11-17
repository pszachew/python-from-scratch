"""
    ogólnie polecam cały ten poradnik do modułu Python Classes/Objects:
    https://www.w3schools.com/python/default.asp

    Zmienne i typy zmiennych w pythonie (podstawowe)
    https://www.w3schools.com/python/python_variables.asp

    lista: https://www.w3schools.com/python/python_lists.asp

    dictionary: https://www.w3schools.com/python/python_dictionaries.asp

"""
# TYPY PODSTAWOWE
x = 5 # typ int
y = 5.2 # typ float (liczba zmiennoprzecinkowa)
z = "ala ma kota" # typ string (tekstowy)

# TYPY ZŁOŻONE
l = [5.2, 1.7, 2.4] # lista złozona z liczb typu float

dictionary = {'first_element': 'text1', 'second_element': 'text2'}
print(dictionary['first_element'])

# Zadeklaruj dwie zmienne typu float o jakichś wartościach, dodaj je do siebie przypisując wynik do trzeciej zmiennej i ją wyświetl
a = 3.2
b = 4.7 
c = a+b
print(c)

t = "Ten tekst zostanie wydrukowany przez funkcję print"
print(t)

print("W ten sposób tez mogę drukować tekst")

# F-string

print(f"wynik dodawania liczby a={a} i b={b} to jest {c}")

var1 = f"wynik dodawania liczby a={a} i b={b} to jest {c}, drugi sposób zapisu poprzez zmienną"
print(var1)

num1 = '23'
num_int = int(num1)
