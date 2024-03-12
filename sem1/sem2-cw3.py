class Car:
    def __init__(self, marka, model, rok):
        self.model=model
        self.rok=rok
        self.marka=marka

car1= Car("BMW","M3", 2004)
car2= Car("Fiat", "126P", 1992)
car3= Car("CZERWONY","ŁADNY", 2000)

print(car1.marka)
print(car2.model)
print(car3.rok)