import sys 
Podaj_liczbe= int(input("Podaj Liczbę do obliczenia w kalkulatorze: "))
Podaj_liczbe2= int(input("Podaj drugą Liczbę do obliczenia w kalkulatorze: "))

Dzialanie= input(f"Co chcesz zrobić z tymi liczbami ,+,-,/,*: ")
Liczby_Do_Sredniej= input("Czy chcesz dodać liczby aby na końcu policzyć średnią z wyniku w kalkulatorze?: T/N:  ")

liczby_do_sredniej = []

if Liczby_Do_Sredniej.lower() == "t":
    ilosc_liczb_do_sredniej = int(input("Podaj ilość liczb do dodania do średniej: "))
    for i in range(ilosc_liczb_do_sredniej):
        liczba_do_sredniej = int(input(f"Podaj {i + 1}. liczbę do średniej: "))
        liczby_do_sredniej.append(liczba_do_sredniej)

if Dzialanie == "+":
    wynik = Podaj_liczbe+Podaj_liczbe2
    print(f'twoja liczba to {wynik}')
elif Dzialanie =="-":
    wynik = Podaj_liczbe-Podaj_liczbe2
    print(f'Twój wynik z odejmoowania to {wynik}, Twoja liczba jest')
elif Dzialanie =="/":
    wynik =Podaj_liczbe/Podaj_liczbe2
    print(f'Twój wynik z odejmoowania to {wynik}')
elif Dzialanie =="*":
    wynik= Podaj_liczbe*Podaj_liczbe2
    print(f'Twój wynik z odejmoowania to {wynik}')
else:
    print("Podaj cyfrę")

wynik += sum(liczby_do_sredniej)

srednia = wynik / (len(liczby_do_sredniej) + 2)


print(f"Średnia arytmetyczna: {srednia}")
p=(input("Czy chcesz teraz spotęgować wynik z sredniej?: T/N"))

potegowanie_input = input("Czy chcesz teraz spotęgować wynik z sredniej?: T/N")

if potegowanie_input.lower() == "t":
    wykladnik = int(input("Podaj wykładnik: "))
    wynik_potegowania = srednia ** wykladnik
    print(f'Wynik potęgowania {srednia} do potęgi {wykladnik} to: {wynik_potegowania}')


if wynik_potegowania %2==0:
    print("Twoja Liczba jest parzysta")
elif wynik_potegowania ==0:
    print("Twoja Liczba nie jest parzysta ani nieparzysta")
else:
    print("Twoja Liczba jest nieparzysta")
fibo = input("Czy Chcesz aby z twojej spotęgowanej liczby obliczyć ciąg fibonacciego? ,T/N")

if fibo.lower() == "t":
        def fibonacci(wynik_potegowania):
            fib_sequence = [0, 1]

            while len(fib_sequence) < wynik_potegowania + 1:
                fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

            return fib_sequence[:int(wynik_potegowania) + 1]


        if wynik_potegowania <= 0:
            print("Podaj liczbę naturalną większą od 0.")
        else:
            result = fibonacci(wynik_potegowania)
            print(f"Ciąg Fibonacciego do {wynik_potegowania}-tego elementu: {result}")

sort = input("Chcesz posortować te liczby?: T/N")

if sort.lower() == "t":
    def sortowanie(result):
        n = len(result)

        while n > 1:
            zamien = False
            for l in range(0, n - 1):
                if result[l] > result[l + 1]:
                    result[l], result[l + 1] = result[l + 1], result[l]
                    zamien = True

            n -= 1
            print(result)
            if not zamien:
                break

        return result

    sorted_result = sortowanie(result)
    print(f"Posortowane liczby: {sorted_result}")


odwrot = input("Czy chcesz teraz odwrócić te liczby?: T/N: ")

if odwrot.lower() == "t":
    reversed_result = list(reversed(sorted_result))
    print(f"Odwrócone liczby: {reversed_result}")

