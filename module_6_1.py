class Animal:
    def __init__(self, name, alive= True, fed= False):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if food.edible is False:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
        if food.edible is True:
            print(f'{self.name} съел {food.name}')
            self.fed = True

class Plant:
    def __init__(self, name, edible= False):
        self.name = name

class Predator(Animal):
    pass

class Mammal(Animal):
    pass

class Flower(Plant):
    def __init__(self, name, edible= False):
        self.name = name
        self.edible = False
class Fruit(Plant):
    def __init__(self, name, edible= True):
        self.name = name
        self.edible = True



animal1 = Predator('Волк с Уолл-Стрит')
animal2 = Mammal('Хатико')
plant1 = Flower('Цветик семицветик')
plant2 = Fruit('Заводной апельсин')

print(animal1.name)
print(plant1.name)

print(animal1.alive)
print(animal2.fed)
animal1.eat(plant1)
animal2.eat(plant2)
print(animal1.alive)
print(animal2.fed)
