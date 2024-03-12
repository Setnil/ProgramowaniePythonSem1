
from pickle import LIST


# Pesel=str(input("Podaj Swój Pesel pierwszy Użytkowniku: "))
# Pesel2=str(input("Podaj Swój Pesel drugi użytkowniku: "))

# Wyciagnij=int(Pesel [0:2])
# Wyciagnij2=int(Pesel2 [0:2])
# print(Wyciagnij)
# print(Wyciagnij2)

# if Wyciagnij<Wyciagnij2:
#     print("Działa Chyba")
# else:
#     print("Chyba tak")


Pesel_again=str(input("Podaj Swój Pesel: "))
Lista_Do_Liczb=[1,3,7,9,1,3,7,9,1,3]
sum=0
licznik=0
for i in Lista_Do_Liczb:
    Wyciagnij=int(Pesel_again[licznik])*int(Lista_Do_Liczb[licznik])
    if int(Pesel_again)==11:
        Wyciagnij=str(Wyciagnij[1])
        suma= suma+int(Wyciagnij)
        print(sum)
    
