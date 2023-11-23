import random

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


F_KWADRATOWA_ROZWIAZANA = False
while F_KWADRATOWA_ROZWIAZANA == False:
    RANDOM_FUNCTION = random.randint(1, ILE_ROWNAN)
    wsp = wspolczynniki[RANDOM_FUNCTION]
    print(f"Podaj najmniejsze rozwiązanie funkcji kwadratowej o wspolczynnikach a={wsp[0]}, b={wsp[1]}, c={wsp[2]}")
    rozwiazanie_uzytkownika = input()
    F_KWADRATOWA_ROZWIAZANA = sprawdz_rozwiazanie_f_kwadratowej(int(rozwiazanie_uzytkownika))
    if F_KWADRATOWA_ROZWIAZANA == True:
        print("To jest dobre rozwiazanie")
    else:
        print("Zle rozwiazanie. Sprobuj jeszcze raz")

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
    else:
        print("Zle rozwiazanie. Sprobuj jeszcze raz")

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
    else:
        print("Zle rozwiazanie, sprobuj ponownie")