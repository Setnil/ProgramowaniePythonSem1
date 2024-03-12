# list1=["styczeń","luty","marzec","kwiecień","luty","luty","maj"]

# list1.append('Listopad')
# list1.pop(0)
# list1.count("styczeń")
# list1.remove(0 :: 1)
# d = 'styczeń' in list1
# list1.reverse()

# unique_list = list(set(list1))

# list1.index("marzec")

# print(unique_list)
# print(list1)
# print(d)


# list1 = ["styczeń", "marzec", "kwiecień", "luty", "maj"]

# parzyste = [list1[i] for i in range(0, len(list1), 2)]

# print(parzyste)

# my_super_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# najm= None
# najw= None

# for  i in my_super_list:
#     if najm == None or najm > i:
#         najm = i


#     if najw == None or najw < i:
#         najw = i

# print(najm)
# print(najw)





# lista1 = ["1styczeń","2luty","3marzec","4kwiecień","5luty","6luty","7maj"]
# middle = int(len(lista1) / 2)
# print(lista1)
 
# nowaLista = [lista1[:middle], lista1[middle:]]
# print(nowaLista)


# my_super_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# suma = 0
# for liczba in my_super_list:
#     suma += liczba

# print("Suma:", suma)


# my_super_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# suma = 0
# for liczba in my_super_list:
#     suma += liczba

# print("Suma:", suma)

# my_super_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# parzyste=0

# for liczba in my_super_list:
#     if liczba % 2== 0:
#         parzyste +=1


# print(parzyste)


# my_super_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# wieksze_sum=0

# for liczba in my_super_list:
#     if liczba > 10:
#         wieksze_sum += liczba


# print(wieksze_sum)
# import sys
# my_super_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# indeks = 0

# for liczba in my_super_list:
#     if liczba == 12:
#         indeks = indeks = my_super_list.index(12)
#         print(indeks)
#         sys.exit(0)


# import sys
# my_super_list = [8,2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 8]

# indeks = 0

# for liczba in my_super_list:
#     if liczba == 8:
#         indeks += 1



# print(indeks)


# my_super_list = [8, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 8]

# indeks = 0

# for liczba in my_super_list:
#     if indeks % 2 != 0:
#         print(f"Element na nieparzystym indeksie {indeks}: {liczba}")
#     indeks += 1


# my_list = [8, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 8]

# najwieksza_liczba = my_list[0]

# for liczba in my_list:
#     if liczba > najwieksza_liczba:
#         najwieksza_liczba = liczba

# print(f"Największa liczba na liście to: {najwieksza_liczba}")


# my_super_list = [8, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 8]

# odwrocona_lista = list(reversed(my_super_list))

# print("oryginalna lista:", my_super_list)
# print("odwrocona lista:", odwrocona_lista)


# my_super_list = [8, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 8]

# liczby_wieksze_niz_10 = []

# for liczba in my_super_list:
#     if liczba > 10:
#         liczby_wieksze_niz_10.append(liczba)

# print(liczby_wieksze_niz_10)


# lista_z_krotkami = [(1, 'jabłko'), (2, 'banan'), (3, 'gruszka'), (4, 'śliwka')]

# # lista_z_krotkami[1] = 'KUKU' - nie da sie dobyr b8
# lista_z_krotkami += [(5, 'winogrono')]
# print(lista_z_krotkami[3])

# print(lista_z_krotkami)

# krotka_do_usuniecia = (4, 'śliwka')
# lista_z_krotkami.remove(krotka_do_usuniecia)
# print(lista_z_krotkami)

moj_slownik = {
    'imie': 'Jan',
    'nazwisko': 'Kowalski',
    'wiek': 30,
    'miasto': 'Warszawa'
}

# print(moj_slownik['imie'])
# moj_slownik['wiek'] = 35
# moj_slownik["email"] ='jan.kowalski@gmail.com'  
# del moj_slownik['miasto']
# print(moj_slownik)

# if 'nazwisko' in moj_slownik:
#     print("Klucz 'nazwisko' istnieje w słowniku.")
# else:
#     print("Klucz 'nazwisko' nie istnieje w słowniku.")


# wartosci = moj_slownik.values()

# print("Wszystkie wartości ze słownika:")
# for wartosc in wartosci:
#     print(wartosc)


moj_slownik = {
    'imie': 'Jan',
    'nazwisko': 'Kowalski',
    'wiek': 35,
    'miasto': 'Warszawa'
}

print("itrenenowanie kluczy:")
for klucz, wartosc in moj_slownik.items():
    print(f"Klucz: {klucz}, Wartość: {wartosc}")


moj_slownik.clear()
print(moj_slownik)