# for i in range(1,11):
#     print(i)


# poprawne_haslo = "tajne_haslo"

# while True:
#     wprowadzone_haslo = input("Podaj hasło: ")

#     if wprowadzone_haslo == poprawne_haslo:
#         print("Poprawne hasło Dostęp udzielony")
#         break
#     else:
#         print("Błędne hasło Spróbuj ponownie")


# while True:
   
#     liczba1 = float(input("Podaj pierwszą liczbę: "))
#     liczba2 = float(input("Podaj drugą liczbę: "))

    
#     print("Wybierz operację:")
#     print("1. Dodawanie")
#     print("2. Odejmowanie")
#     print("3. Mnożenie")
#     print("4. Dzielenie")
#     print("5. Zakończ program")

#     operacja = input("Podaj numer operacji: ")

    
#     if operacja == "1":
#         wynik = liczba1 + liczba2
#         print("Wynik dodawania:", wynik)
#     elif operacja == "2":
#         wynik = liczba1 - liczba2
#         print("Wynik odejmowania:", wynik)
#     elif operacja == "3":
#         wynik = liczba1 * liczba2
#         print("Wynik mnożenia:", wynik)
#     elif operacja == "4":
#         if liczba2 != 0:
#             wynik = liczba1 / liczba2
#             print("Wynik dzielenia:", wynik)
#         else:
#             print("Nie można dzielić przez zero.")
#     elif operacja == "5":
#         print("Zakończono program.")
#         break
#     else:
#         print("Nieprawidłowy numer operacji. Spróbuj ponownie.")

# import random

# liczba_prob = 5
# maksymalna_liczba_prob = 0

# while liczba_prob > maksymalna_liczba_prob:
    
#     wprowadzona_liczba = input("Podaj liczbę całkowitą od 1 do 100: ")
    
    
#     try:
#         wprowadzona_liczba = int(wprowadzona_liczba)
#     except ValueError:
#         print("To nie jest liczba")
#         continue
    
   
#     losowa_liczba = random.randint(1, 100)
#     if losowa_liczba == wprowadzona_liczba:
#         print("Zgadłeś")
#     else:
#         print("próbuj dalej twoja liczba prób to, ", liczba_prob)
    
    
#     liczba_prob -= 1

# print("Koniec programu")

import random

lista =("dupa", "xD", "jd","Xd","NIEWIEM","JEZUUU")

lista = random.choice(lista)

slowo_do_zgadniecie= lista
punkty= 0


while punkty <5:
    choice1= input("Podaj słowo do zgandięcia: ")
    if choice1 in slowo_do_zgadniecie:
        print("zgadłeś w ", punkty ,"próbach")
        break
    else:
        print("próbuj dalej, słowo do zgadnięcia jest na", len(slowo_do_zgadniecie), "litery")
        punkty+=1