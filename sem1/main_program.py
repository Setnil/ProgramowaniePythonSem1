# main_program_dynamic.py


from my_library import dodaj_liczby
from my_library import odejmij_liczby, pomnoz_liczby, zapytaj_o_liczbe, zapytaj_o_liczbe2


nazwy_funkcji = ['zapytaj_o_liczbe', 'zapytaj_o_liczbe2', 'dodaj_liczby', 'odejmij_liczby', 'pomnoz_liczby']


for nazwa_funkcji in nazwy_funkcji:
    import_statement = f'from my_library import {nazwa_funkcji}'
    exec(import_statement)


liczba1 = zapytaj_o_liczbe()
liczba2 = zapytaj_o_liczbe2()

wynik_dodawania = dodaj_liczby(liczba1, liczba2)
wynik_odejmowania = odejmij_liczby(liczba1, liczba2)
wynik_mnozenia = pomnoz_liczby(liczba1, liczba2)

print(f"Wynik dodawania {liczba1} i {liczba2} to: {wynik_dodawania}")
print(f"Wynik odejmowania {liczba1} i {liczba2} to: {wynik_odejmowania}")
print(f"Wynik mnożenia {liczba1} i {liczba2} to: {wynik_mnozenia}")
