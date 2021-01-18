class Cats:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def getname(self):
        return self.name

    def getgender(self):
        return self.gender

    def getage(self):
        return self.age

from cat import Cats

cat_1 = Cats('Барон', 'мальчик', '2')
cat_2 = Cats('Сэм', 'мальчик', '2')

pets = [cat_1, cat_2]

for pet in pets:
    pet.print_list()