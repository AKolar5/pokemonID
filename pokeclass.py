class Type:
    def __init__(self, name, weak, resist, supeff, noteff, counter, immune):
        self.name = name
        self.weak = weak
        self.resist = resist
        self.supeff = supeff
        self.noteff = noteff
        self.counter = counter
        self.immune = immune

    def getName(self):
        return self.name

    def getWeak(self):
        return self.weak

    def getResist(self):
        return self.resist

    def getSupeff(self):
        return self.supeff

    def getNoteff(self):
        return self.noteff

    def getCounter(self):
        return self.counter

    def getImmune(self):
        return self.immune


class Bug(Type):
    def __init__(self):
        self.name = 'Bug'
        self.weak = ['Fire', 'Flying', 'Rock']
        self.resist = ['Fighting', 'Grass', 'Ground']
        self.supeff = ['Dark', 'Grass', 'Psychic']
        self.noteff = ['Fairy', 'Fighting', 'Fire', 'Flying', 'Ghost', 'Poison', 'Steel']
        self.counter = ['Fire', 'Flying']
        self.immune = []

class Dark(Type):
    def __init__(self):
        self.name = 'Dark'
        self.weak = ['Bug', 'Fairy', 'Fighting']
        self.resist = ['Dark', 'Ghost', 'Psychic']
        self.supeff = ['Ghost', 'Psychic']
        self.noteff = ['Dark', 'Fairy', 'Fighting']
        self.counter = ['Fairy', 'Fighting']
        self.immune = ['Psychic']

class Dragon(Type):
    def __init__(self):
        self.name = 'Dragon'
        self.weak = ['Dragon', 'Fairy', 'Ice']
        self.resist = ['Fire', 'Grass', 'Electric', 'Water']
        self.supeff = ['Dragon']
        self.noteff = ['Fairy', 'Steel']
        self.counter = ['Fairy']
        self.immune = []

class Electric(Type):
    def __init__(self):
        self.name = 'Electric'
        self.weak = ['Ground']
        self.resist = ['Electric', 'Flying', 'Steel']
        self.supeff = ['Flying', 'Water']
        self.noteff = ['Dragon', 'Electric', 'Grass', 'Ground']
        self.counter = ['Ground']
        self.immune = []

class Fairy(Type):
    def __init__(self):
        self.name = 'Fairy'
        self.weak = ['Poison', 'Steel']
        self.resist = ['Bug', 'Dark', 'Dragon', 'Fighting']
        self.supeff = ['Dark', 'Dragon', 'Fighting']
        self.noteff = ['Fairy', 'Fighting', 'Fire', 'Flying', 'Ghost', 'Poison', 'Steel']
        self.counter = ['Fire', 'Flying', 'Steel']
        self.immune = ['Dragon']

class Fighting(Type):
    def __init__(self):
        self.name = 'Fighting'
        self.weak = ['Fairy', 'Flying', 'Psychic']
        self.resist = ['Bug', 'Dark', 'Rock']
        self.supeff = ['Dark', 'Ice', 'Normal', 'Rock', 'Steel']
        self.noteff = ['Bug', 'Fairy', 'Flying', 'Ghost', 'Poison', 'Psychic']
        self.counter = ['Fairy', 'Flying', 'Psychic']
        self.immune = []

class Fire(Type):
    def __init__(self):
        self.name = 'Fire'
        self.weak = ['Ground', 'Rock', 'Water']
        self.resist = ['Bug', 'Fairy', 'Fire', 'Grass', 'Ice', 'Steel']
        self.supeff = ['Bug', 'Grass', 'Ice', 'Steel']
        self.noteff = ['Dragon', 'Fire', 'Rock', 'Water']
        self.counter = ['Rock', 'Water']
        self.immune = []

class Flying(Type):
    def __init__(self):
        self.name = 'Flying'
        self.weak = ['Electric', 'Ice', 'Rock']
        self.resist = ['Bug', 'Fighting', 'Grass', 'Ground']
        self.supeff = ['Bug', 'Fighting', 'Grass']
        self.noteff = ['Electric', 'Rock', 'Steel']
        self.counter = ['Electric', 'Rock']
        self.immune = ['Ground']

class Ghost(Type):
    def __init__(self):
        self.name = 'Ghost'
        self.weak = ['Dark', 'Ghost']
        self.resist = ['Bug', 'Fighting', 'Normal', 'Poison']
        self.supeff = ['Ghost', 'Psychic']
        self.noteff = ['Dark', 'Normal']
        self.counter = ['Dark']
        self.immune = ['Fighting', 'Normal']

class Grass(Type):
    def __init__(self):
        self.name = 'Grass'
        self.weak = ['Bug', 'Fire', 'Flying', 'Ice', 'Poison']
        self.resist = ['Electric', 'Grass', 'Ground', 'Water']
        self.supeff = ['Ground', 'Rock', 'Water']
        self.noteff = ['Bug', 'Dragon', 'Fire', 'Flying', 'Grass', 'Poison', 'Steel']
        self.counter = ['Bug', 'Fire', 'Flying', 'Poison']
        self.immune = []

class Ground(Type):
    def __init__(self):
        self.name = 'Ground'
        self.weak = ['Grass', 'Ice', 'Water']
        self.resist = ['Electric', 'Poison', 'Rock']
        self.supeff = ['Electric', 'Fire', 'Poison', 'Rock', 'Steel']
        self.noteff = ['Bug', 'Flying', 'Grass']
        self.counter = ['Grass']
        self.immune = ['Electric']

class Ice(Type):
    def __init__(self):
        self.name = 'Ice'
        self.weak = ['Fighting', 'Fire', 'Rock', 'Steel']
        self.resist = ['Ice']
        self.supeff = ['Dragon', 'Flying', 'Grass', 'Ground']
        self.noteff = ['Fire', 'Ice', 'Steel', 'Water']
        self.counter = ['Fire', 'Steel']
        self.immune = []

class Normal(Type):
    def __init__(self):
        self.name = 'Normal'
        self.weak = ['Fighting']
        self.resist = ['Ghost']
        self.supeff = []
        self.noteff = ['Ghost', 'Rock', 'Steel']
        self.counter = []
        self.immune = ['Ghost']

class Poison(Type):
    def __init__(self):
        self.name = 'Poison'
        self.weak = ['Ground', 'Psychic']
        self.resist = ['Bug', 'Fairy', 'Fighting', 'Grass', 'Poison']
        self.supeff = ['Fairy', 'Grass']
        self.noteff = ['Ghost', 'Ground', 'Poison', 'Rock', 'Steel']
        self.counter = ['Ground']
        self.immune = []

class Psychic(Type):
    def __init__(self):
        self.name = 'Psychic'
        self.weak = ['Bug', 'Dark', 'Ghost']
        self.resist = ['Fighting', 'Psychic']
        self.supeff = ['Fighting', 'Poison']
        self.noteff = ['Dark', 'Psychic', 'Steel']
        self.counter = ['Dark']
        self.immune = []

class Rock(Type):
    def __init__(self):
        self.name = 'Rock'
        self.weak = ['Fighting', 'Grass', 'Ground', 'Steel', 'Water']
        self.resist = ['Fire', 'Flying', 'Normal', 'Poison']
        self.supeff = ['Bug', 'Fire', 'Flying', 'Ice']
        self.noteff = ['Fighting', 'Ground', 'Steel']
        self.counter = ['Fighting', 'Ground', 'Steel']
        self.immune = []

class Steel(Type):
    def __init__(self):
        self.name = 'Steel'
        self.weak = ['Fire', 'Fighting', 'Ground']
        self.resist = ['Bug', 'Dragon', 'Fairy', 'Flying', 'Grass', 'Ice', 'Normal', 'Poison', 'Psychic', 'Rock']
        self.supeff = ['Fairy', 'Ice', 'Rock']
        self.noteff = ['Electric', 'Fire', 'Water']
        self.counter = ['Fire']
        self.immune = ['Poison']

class Water(Type):
    def __init__(self):
        self.name = 'Water'
        self.weak = ['Grass', 'Electric']
        self.resist = ['Fire', 'Ice', 'Steel', 'Water']
        self.supeff = ['Fire', 'Ground', 'Rock']
        self.noteff = ['Dragon', 'Grass', 'Water']
        self.counter = ['Grass']
        self.immune = []




def makePoke(type1):
    if type1.lower() == 'bug':
        return Bug()
    if type1.lower() == 'dark':
        return Dark()
    if type1.lower() == 'dragon':
        return Dragon()
    if type1.lower() == 'electric':
        return Electric()
    if type1.lower() == 'fairy':
        return Fairy()
    if type1.lower() == 'fighting':
        return Fighting()
    if type1.lower() == 'fire':
        return Fire()
    if type1.lower() == 'flying':
        return Flying()
    if type1.lower() == 'ghost':
        return Ghost()
    if type1.lower() == 'grass':
        return Grass()
    if type1.lower() == 'ground':
        return Ground()
    if type1.lower() == 'ice':
        return Ice()
    if type1.lower() == 'normal':
        return Normal()
    if type1.lower() == 'poison':
        return Poison()
    if type1.lower() == 'psychic':
        return Psychic()
    if type1.lower() == 'rock':
        return Rock()
    if type1.lower() == 'steel':
        return Steel()
    if type1.lower() == 'water':
        return Water()

def compare(onew, oner, twow, twor):
    c = []
    for i in onew:
        if i not in twor:
            if i not in c:
                c.append(i)

    for i in twow:
        if i not in oner:
            if i not in c:
                c.append(i)

    return c

def findCounter(weak, notff):
    m = []

    for i in weak:
        if i in notff:
            if i not in m:
                m.append(i)

    return m

def compareCounter(type1, type2):
    m = []
    for i in type1.getCounter():
        if i in type2.getResist():
            type1.getCounter().remove(i)

    for i in type1.getCounter():
        if i in type2.getSupeff():
            type1.getCounter().remove(i)

    for i in type2.getCounter():
        if i in type1.getResist():
            type2.getCounter().remove(i)

    for i in type2.getCounter():
        if i in type1.getSupeff():
            type2.getCounter().remove(i)

    for i in type1.getCounter():
        if i not in m:
            m.append(i)

    for i in type2.getCounter():
        if i not in m:
            m.append(i)

    return m

def combine(list1, list2):
    m = []
    if len(list1) + len(list2) == 0:
        return 'None'
    else:
        for i in list1:
            if i not in m:
                m.append(i)

        for i in list2:
            if i not in m:
                m.append(i)

        return m

def isListEmpty(list):
    if len(list) == 0:
        return True
    else:
        return False

