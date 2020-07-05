all_weights = []
max_weight = dict()


class Animal:
    def eat(self):
        print('I eat')


class Milk(Animal):
    def milking(self):
        print('Hello, you can milk me if you want')


class Eggs(Animal):
    def collect_eggs(self):
        print('Hey! Collect my eggs if you want!')


class Goose(Eggs):
    sound = 'Ga-ga'
    body = '2 wings and 2 feet'

    def __init__(self, name, weight=3):
        self.name = name
        self.weight = weight
        all_weights.append(self.weight)
        max_weight[self.name] = self.weight


grey_goose = Goose('Serik')
white_goose = Goose('Belik')


class Cow(Milk):
    sound = 'Mu'
    body = '2 horns, 4 feet'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        all_weights.append(self.weight)
        max_weight[self.name] = self.weight


Manka = Cow('Manka', 130)


class Sheep(Animal):
    sound = 'Meee'
    body = '4 feet, wool'

    def shave(self):
        print('Hey! Shave me if I am ready for that!')

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        all_weights.append(self.weight)
        max_weight[self.name] = self.weight


bar = Sheep('barashek', 49)
kudr = Sheep('kudrjashek', 51)


class Chicken(Eggs):
    sound = 'kokoko'
    body = 'beak and feathers'

    def __init__(self, name, weight=2):
        self.name = name
        self.weight = weight
        all_weights.append(self.weight)
        max_weight[self.name] = self.weight


chicken1 = Chicken('kukareku')
chicken2 = Chicken('chip-chip')


class Goat(Milk):
    sound = ' Me'
    body = 'horns and hooves'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        all_weights.append(self.weight)
        max_weight[self.name] = self.weight


goat1 = Goat('Kozi', 37)
goat2 = Goat('Koza', 42)


class Dug(Eggs):
    sound = 'krja-krja'
    body = 'yellow beak'

    def __init__(self, name, weight=5):
        self.name = name
        self.weight = weight
        all_weights.append(self.weight)
        max_weight[self.name] = self.weight


dug1 = Dug('Utkonos')
dug2 = Dug('Utka')

big = [(values, keys) for keys, values in max_weight.items()]

print(f'Общий вес животных: {sum(all_weights)}. Cамое тяжелое животное: {max(big)[1]}')