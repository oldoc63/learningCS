class Pokemon:
    def __init__(self, name, type, level=5):
        self.name = name
        self.level = level
        self.health = level * 5
        self.max_health = level * 5
        self.type = type
        self.is_knocked_out = False

    def __repr__(self):
        return f'This level {self.level} name {self.name} has {self.health} hit points remaining. They are a {self.type} type Pokemon'

    def revive(self):
        self.is_knocked_out = False
        if self.health == 0:
            self.health = 1
        print(f'{self.name} was revived!')
    
    def knock_out(self):
        self.is_knocked_out = True
        if self.health != 0:
            self.health = 0
        print(f'{self.name} was knocked out!')

    def lose_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.knock_out()
        else:
            print(f'{self.name} now has health {self.health}.')

    def gain_health(self, amount):
        if self.health == 0:
            self.revive()
        self.health += amount
        if self.health >= self.max_health:
            self.health = self.max_health
        print(f'{self.name} now has {self.health} health.')

# Six pokemon are made with different levels. (If no level is given, it is level 5)
a = Pokemon("Charmander", "Fire", 7)
b = Pokemon("Squirtle", "Water")
c = Pokemon("Lapras", "Water", 9)
d = Pokemon("Bulbasaur", "Grass", 10)
e = Pokemon("Vulpix", "Fire")
f = Pokemon("Staryu", "Water", 4)

print(a.health)

a.lose_health(10)
a.lose_health(10)
a.lose_health(10)
a.lose_health(10)
a.gain_health(1)
a.gain_health(34)

print(a.health)
