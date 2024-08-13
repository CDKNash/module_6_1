class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name

class Plant:
    edible = False
    def __init__(self, name):
        self.name = name

class Predator(Animal):
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        self.food = plant1
        print(f'{self.name} не стал есть {food.name}')
    alive = False

class Mammal(Animal):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        self.food = plant2
        print(f'{self.name} съел {food.name}')
    fed = True

class Flower(Plant):
    def __init__(self, name):
        self.name = name

class Fruit(Plant):
    edible = True
    def __init__(self, name):
        self.name = name


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
