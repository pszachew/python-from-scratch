import random

POPRAWNE = 0
ZLE = 0
MAX_ZLE = 10
PIERWSZA_ZAKRES = 100

wspolczynniki = {
    1: [1, 5, 6],
    2: [-1, 5, -6],
    3: [1, 1, -2]
}

ILE_ROWNAN = len(wspolczynniki)

rozwiazania = {
    1: [-2, -3],
    2: [2, 3],
    3: [-2, 1]
}


def generuj_liczby(n):
    ls = []
    for i in range(n):
        x = random.randint(1, 50)
        ls.append(x)
    return ls


def sprawdz_rozwiazanie_f_kwadratowej(x):
    poprawne_rozwiazania = rozwiazania[RANDOM_FUNCTION]
    najmniejsze = min(poprawne_rozwiazania)
    if x == najmniejsze:
        return True
    else:
        return False


def sprawdz_rozwiazanie_prostokata(a, b, wartosc, flaga):
    if flaga == "obwód":
        if 2*a + 2*b == wartosc:
            return True
        else:
            return False
    elif flaga == "pole":
        if a*b == wartosc:
            return True
        else:
            return False


def czy_pierwsza(x):
    pierwsza = True
    for i in range(2, int(x/2) + 1):
        if x % i == 0:
            pierwsza = False
    return pierwsza


rozwiazanie_podzielne = False
while rozwiazanie_podzielne == False:
    liczby = generuj_liczby(10)
    print(f"Z podanych liczb {liczby} wpisz pozycje tych liczb (zaczynajac od 0), które są podzielne przez 3. Poszczegolne liczby oddziel spacja")
    user_input = input()
    user_input = user_input.strip() # usuwa białe znaki z końca inputu
    user_input = user_input.split(" ")
    print(user_input)
    wszystkie_podzielne = True
    user_input = [int(x) for x in user_input]
    print(user_input)
    for el in user_input:
        if liczby[int(float(el))] % 3 != 0:
            wszystkie_podzielne = False
    if wszystkie_podzielne == True:
        rozwiazanie_podzielne = True
        print("To dobre rozwiazanie")
        POPRAWNE += 1
    else:
        ZLE += 1
        if ZLE == MAX_ZLE:
            print("Wykorzystales wszystkie szanse. Przegrales gre.")
            exit()
        else:
            print(f"Zle rozwiazanie. Sprobuj jeszcze raz. Masz jeszcze {MAX_ZLE - ZLE} szans.")

rozwiazanie_pierwsze = False
while rozwiazanie_pierwsze == False:
    pierwsza_rand = random.randint(1, PIERWSZA_ZAKRES)
    print(f"Czy liba {pierwsza_rand} jest liczba pierwsza? jesli tak wpisz w konsoli 1, w przeciwnym przypadku wpisz 0")
    user_input = input()
    if czy_pierwsza(pierwsza_rand) == True and int(user_input) == 1:
        rozwiazanie_pierwsze = True
        print("To dobre rozwiazanie")
        POPRAWNE += 1
    elif czy_pierwsza(pierwsza_rand) == False and int(user_input) == 0:
        rozwiazanie_pierwsze = True
        print("To dobre rozwiazanie")
        POPRAWNE += 1
    else:
        ZLE += 1
        if ZLE == MAX_ZLE:
            print("Wykorzystales wszystkie szanse. Przegrales gre.")
            exit()
        else:
            print(f"Zle rozwiazanie. Sprobuj jeszcze raz. Masz jeszcze {MAX_ZLE - ZLE} szans.")



F_KWADRATOWA_ROZWIAZANA = False
while F_KWADRATOWA_ROZWIAZANA == False and ZLE < MAX_ZLE:
    RANDOM_FUNCTION = random.randint(1, ILE_ROWNAN)
    wsp = wspolczynniki[RANDOM_FUNCTION]
    print(f"Podaj najmniejsze rozwiązanie funkcji kwadratowej o wspolczynnikach a={wsp[0]}, b={wsp[1]}, c={wsp[2]}")
    rozwiazanie_uzytkownika = input()
    F_KWADRATOWA_ROZWIAZANA = sprawdz_rozwiazanie_f_kwadratowej(int(rozwiazanie_uzytkownika))
    if F_KWADRATOWA_ROZWIAZANA == True:
        print("To jest dobre rozwiazanie")
        POPRAWNE += 1
    else:
        ZLE += 1
        if ZLE != MAX_ZLE:
            print(f"Zle rozwiazanie. Sprobuj jeszcze raz. Masz jeszcze {MAX_ZLE - ZLE} szans.")
    if ZLE == MAX_ZLE:
        print("Wykorzystales wszystkie szanse. Przegrales gre.")
        exit()


wymiary_prostokata = {
    1: [1, 2],
    2: [3, 5],
    3: [9, 2]
}

OBWOD_CZY_POLE = {
    0: "obwód",
    1: "pole"
}
rozwiazanie_prostokata = False

while rozwiazanie_prostokata == False:
    WYMIARY_WYLOSOWANE = random.randint(1, len(wymiary_prostokata)) 
    WYMIARY = wymiary_prostokata[WYMIARY_WYLOSOWANE]

    OBWOD_CZY_POLE_FLAGA = random.randint(0, 1)

    OBWOD_POLE_STR = OBWOD_CZY_POLE[OBWOD_CZY_POLE_FLAGA]
    print(f"Oblicz {OBWOD_POLE_STR} prostokata o wymiarach a={WYMIARY[0]}, b={WYMIARY[1]}")
    wartosc = input()
    rozwiazanie_prostokata = sprawdz_rozwiazanie_prostokata(a=WYMIARY[0], b=WYMIARY[1], wartosc=int(wartosc), flaga=OBWOD_POLE_STR)
    if rozwiazanie_prostokata == True:
        print("Dobre rozwiazanie")
        POPRAWNE += 1
    else:
        ZLE += 1
        if ZLE == MAX_ZLE:
            print("Wykorzystales wszystkie szanse. Przegrales gre.")
            exit()
        else:
            print(f"Zle rozwiazanie. Sprobuj jeszcze raz. Masz jeszcze {MAX_ZLE - ZLE} szans.")

NWW = {
    1: [2, 8],
    2: [7, 10],
    3: [8, 12]
}

NWW_ROZWIAZANIA = {
    1: 8,
    2: 70,
    3: 24
}

rozwiazanie_nww = False
while rozwiazanie_nww == False:
    NWW_RAND = random.randint(1, len(NWW))
    liczby = NWW[NWW_RAND]
    print(f"Podaj NWW dla liczb a={liczby[0]}, b={liczby[1]}")
    wartosc = input()
    if int(wartosc) == NWW_ROZWIAZANIA[NWW_RAND]:
        rozwiazanie_nww = True
        print("To dobre rozwiazanie")
        POPRAWNE += 1
    else:
        ZLE += 1
        if ZLE == MAX_ZLE:
            print("Wykorzystales wszystkie szanse. Przegrales gre.")
            exit()
        else:
            print(f"Zle rozwiazanie. Sprobuj jeszcze raz. Masz jeszcze {MAX_ZLE - ZLE} szans.")


NWD = {
    1: [2, 8],
    2: [7, 10],
    3: [8, 12]
}

NWD_ROZWIAZANIA = {
    1: 2,
    2: 1,
    3: 4
}

rozwiazanie_nwd = False
while rozwiazanie_nwd == False:
    NWD_RAND = random.randint(1, len(NWD))
    liczby = NWD[NWD_RAND]
    print(f"Podaj NWD dla liczb a={liczby[0]}, b={liczby[1]}")
    wartosc = input()
    if int(wartosc) == NWD_ROZWIAZANIA[NWD_RAND]:
        rozwiazanie_nwd = True
        print("To dobre rozwiazanie")
        POPRAWNE += 1
    else:
        ZLE += 1
        if ZLE == MAX_ZLE:
            print("Wykorzystales wszystkie szanse. Przegrales gre.")
            exit()
        else:
            print(f"Zle rozwiazanie. Sprobuj jeszcze raz. Masz jeszcze {MAX_ZLE - ZLE} szans.")

