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
    
    def attack(self, other_pokemon):
        if self.is_knocked_out:
            print(f"{self.name} cant't attack because it is knocked out")
            return

        if (self.type == "Fire" and other_pokemon.type == "Water") or (self.type == "Water" and other_pokemon.type == "Grass") or (self.type == "Grass" and other_pokemon.type == "Fire"):
            print(f'{self.name} attacked {other_pokemon.name} for {round(self.level * 0.5)} damage.')
            print('Its not very effective')
            other_pokemon.lose_health(round(self.level * 0.5))
            
        if (self.type == other_pokemon.type):
            print(f'{self.name} attacked {other_pokemon.name} for {self.level} damage.')
            other_pokemon.lose_health(self.level)

        if (self.type == "Fire" and other_pokemon.type == "Grass") or (self.type == "Water" and other_pokemon.type == "Fire") or (self.type == "Grass" and other_pokemon.type == "Water"):
            print(f'{self.name} attacked {other_pokemon.name} for {self.level * 2} damage.')
            print("It's super effective")
            other_pokemon.lose_health(self.level * 2)

class Trainer:
    def __init__(self, pokemon_list, num_potions, name):
        self.pokemons = pokemon_list
        self.potions = num_potions
        self.current_pokemon = 0
        self.name = name

    def __repr__(self):
        print(f'The trainer {self.name} has the following pokemon')
        for pokemon in self.pokemons:
            print(pokemon)
        return f'The current active pokemon is {self.pokemons[self.current_pokemon].name}'
            
    def switch_active_pokemon(self, new_active):
        if new_active < len(self.pokemons) and new_active >= 0:
            if self.pokemons[new_active].is_knocked_out:
                print(f"{self.pokemons[new_active].name} and is knocked out. You can't make it your active pokemon")
            elif new_active == self.current_pokemon:
                print(f'{self.pokemons[new_active].name} and is already your active pokemon')
            else:
                self.current_pokemon = new_active
                print(f"Go {self.pokemons[self.current_pokemon].name}, it's your turn!")

    def use_potion(self):
        if self.potions > 0:
            print(f'You used a potion on {self.pokemons[self.current_pokemon].name}')
            self.pokemons[self.current_pokemon].gain_health(20)
            self.potions -= 1
        else:
            print("You don't have any more potions")    

# Six pokemon are made with different levels. (If no level is given, it is level 5)
a = Pokemon("Charmander", "Fire", 7)
b = Pokemon("Squirtle", "Water")
c = Pokemon("Lapras", "Water", 9)
d = Pokemon("Bulbasaur", "Grass", 10)
e = Pokemon("Vulpix", "Fire")
f = Pokemon("Staryu", "Water", 4)


trainer1 = Trainer([a,b,c], 2, 'Leo')
print(trainer1)
trainer1.switch_active_pokemon(1)
trainer1.use_potion()
