class Osoba:
    def __init__(self, name, secondname, age):
        self.name=name
        self.secondname=secondname
        self.age=age

p1= Osoba("Janek","Kowalski", 666)

print(p1.name)
print(p1.secondname)
print(p1.age)