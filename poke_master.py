# Create a Pokémon class.
# The __init__() method of our Pokémon class created variables to keep track
# of the Pokémon’s name, level, type (for example "Fire" or "Water"), maximum health,
# current health, and whether or not the Pokémon was knocked out.
# In our implementation, the maximum health was determined by the Pokémon’s level.

# can't use "type" in the __init__ definitition because type already has a default usage
# so I used "element" instead

#                                   ,'\
#     _.----.        ____         ,'  _\   ___    ___     ____
# _,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
# \      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
#  \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
#    \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
#     \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
#      \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
#       \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
#        \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
#         \_.-'       |__|    `-._ |              '-.|     '-.| |   |
#                                 `'                            '-._|


import random


class Pokemon:
    def __init__(self, name, level, element, current_health=100, awake_asleep=True, max_health=None):
        self.name = name
        self.level = level
    # for this instance we're going to use levels 1-100
        self.element = element
        self.current_health = current_health
        self.awake = awake_asleep
    # we're also going to assume that max_health = 100 except if unspecified it's the amount of the level
        if max_health == None:
            self.max_health = self.level
        else:
            self.max_health = max_health

    def __repr__(self):
        return f"""
        {self.name}
        LV {self.level}
        Type: {self.element}
        HP {self.current_health}/100
        {self.name} is awake? {self.awake}
        """

# add a __repr__ method that prints the stats of the Pokemon currently
# COMPLETE

# !!! change awake_asleep to True/False so you can check KO
# COMPLETE

# now we are basically writing a fancy text based roleplay to fight pokemon
# this means we need to hurt, heal, KO, and revive

# how do I make a running mutable value for health that the following method can change?
# jeff doesn't think I need to so I'll try it without
# that totally worked

# now, how do I get it so current health has a min of 0 and max of 100?
# !!! fix this -- write a new method that does this functionality
# !!! then call that method inside other methods
# COMPLETE

    def health_check(self):
        if self.current_health < 0:
            self.current_health = 0
        if self.current_health > 100:
            self.current_health = 100
        return self.current_health


# I also need to write in functionality so that two pokemon can attack each other
# such as instantiating two different pokemon and having them attack each other
# okay that's working other than printing the __repr__ at the instance of self.name??
# totally got that working by using the .name for the enemy as well


    def knock_out(self):
        self.health_check()
        if self.current_health <= 0:
            self.awake = False
            print(f'{self.name} has been knocked out!')
        else:
            print(f"{self.name} is awake and has {self.current_health} HP.")

    def revive(self, revive_value=100):
        self.awake = True
        self.current_health += revive_value
        self.health_check()
        print(f'{self.name} has been revived to {self.current_health} HP!')

# okay my problem here is I wrote the following as the self being acted UPON
# they're asking for the self to do the acting
# so I need to rewrite this
    # def attacked_by(self, enemy_name, attack_value=None):
    #     if attack_value == None:
    #         attack = random.randint(0,100)
    #     else:
    #         attack = attack_value

    #     self.current_health -= attack
    #     self.health_check()
    #     if self.current_health <= 0:
    #         self.knock_out()

    #     print(f"{enemy_name.name} has attacked {self.name}! {self.name}'s health is reduced to {self.current_health}!")

    # THIS WASN'T A GOOD STRUCTURE SO I REMADE IT ENTIRELY AS BELOW
    # Fire = {"advantage": "Grass", "disadvantage": "Water"}
    # Water = {"advantage": "Fire", "disadvantage": "Grass"}
    # Grass = {"advantage": "Water", "disadvantage": "Fire"}
    # If we ever want to add more types where the advantages stack, make the value a list???

    advantage = {"Fire": "Grass", "Water": "Fire", "Grass": "Water"}
    disadvantage = {"Fire": "Water", "Water": "Grass", "Grass": "Fire"}

    def advantage_check(self, enemy):

        if self.advantage[self.element] == enemy.element:
            print(f"{self.name} has an advantage over {enemy.name}!")
            return 2
        if self.disadvantage[self.element] == enemy.element:
            print(f"{self.name} is at a disadvantage against {enemy.name}!")
            return 0.5
        if self.advantage[self.element] != enemy.element and self.disadvantage[self.element] != enemy.element:
            return 1


# FIRST FAILED ATTEMPT AT THE ADVANTAGE CHECK, DO NOT USE THIS ONE
    # advantage_dict = [Fire, Water, Grass]

    # def advantage_check(self, enemy):

    #     if self.element == "Fire":
    #         if self.Fire["advantage"] == enemy.element():
    #             return 2
    #         elif self.Fire["disadvantage"] == enemy.element():
    #             return 0.5

    #     elif self.element == "Water":

    #         if self.Water["advantage"] == enemy.element():
    #             return 2
    #         elif self.Water["disadvantage"] == enemy.element():
    #             return 0.5

    #     elif self.element == "Grass":

    #         if self.Grass["advantage"] == enemy.element():
    #             return 2
    #         elif self.Grass["disadvantage"] == enemy.element():
    #             return 0.5


    def attacks(self, enemy, attack_value=None):
        if attack_value == None:
            base_attack = random.randint(0, 100)
        else:
            base_attack = attack_value

        # print(base_attack)
        # now we need to check for advantage
        damage = self.advantage_check(enemy)
        attack = (base_attack * damage)
        # print(attack)

        # this is checking if you're attacking a fainted pokemon
        if enemy.current_health <= 0:
            print(f"{enemy.name} is already knocked out!")
        else:
            enemy.current_health -= attack
            enemy.health_check()
            print(
                f"{self.name} attacks {enemy.name}! {enemy.name}'s health is reduced to {enemy.current_health}!")

            # this checks if you've KOd the opponent with the attack
            if enemy.current_health <= 0:
                enemy.knock_out()

    # okay now I gotta figure out how to stop this function from happening if the enemy is KOd
    # COMPLETE

    def heal(self, healing_potion_value=None):
        if healing_potion_value == None:
            heal = random.randint(0, 100)
        else:
            heal = healing_potion_value

        self.current_health += heal
        self.health_check()

        print(f"{self.name} has been healed to {self.current_health} HP!")

# listing active Pokemon as 1-6 as per the list


class Trainer():
    def __init__(self, name, potions=[], pokemon=[], current_pokemon=None):
        self.name = name
        self.potions = potions
        self.pokemon = pokemon
        if self.pokemon != []:
            self.current_pokemon = self.pokemon[0]
        else:
            self.current_pokemon = current_pokemon

    def attack(self, trainer):
        pass

    def use_potion(self, pokemon):
        pass

    def switch_pokemon(self, new_pokemon):
        pass

    def catch_pokemone(self, ):
        #         if self.pokemon != []:
        # self.current_pokemon = self.pokemon[0]
        pass

    def __repr__(self):
        list_pokemon_names = ""
        for i in self.pokemon:
            list_pokemon_names = list_pokemon_names + i.name + ', '
        return f'''
        Name: {self.name}
        Current Pokemon: {self.current_pokemon}
        Potions: {self.potions}
        Pokemon: {list_pokemon_names}
        '''


# here's my little test section! let's see if things are working!
# test class instantiation
Cyndaquil = Pokemon("Cyndaquil", 40, "Fire", 100)
Totodile = Pokemon("Totodile", 50, "Water", 100)
Charmander = Pokemon("Charmander", 60, "Fire")
# print(Cyndaquil)
# this test worked and I got the __repr__ method to work with strings
# print(Cyndaquil.name)
# print(Cyndaquil.level)
# print(Cyndaquil.element)
# print(Cyndaquil.current_health)
# print(Cyndaquil.max_health)

# test Trainer instantiation
Ash = Trainer("Ash", pokemon=[Cyndaquil, Totodile, Charmander], potions=[
              "heal", "revive", "antidote", "burn salve"])
print(Ash)

# fix the problem with the advantage/disadvantage chart if the pokemon's element
# doesn't appear within the chart
# ie for Pikachu
# I think i fixed this 6.26.20


# TESTING THE ATTACK FUNCTION WITH ALL FUNCTIONALITY

# Cyndaquil.attacks(Totodile)
# Totodile.attacks(Cyndaquil)
# Totodile.attacks(Cyndaquil)
# Totodile.attacks(Cyndaquil)
# Totodile.attacks(Cyndaquil)
# Totodile.attacks(Cyndaquil)
# Cyndaquil.revive()
# print(Cyndaquil.health_check())
# Cyndaquil.knock_out()
# Cyndaquil.revive()
# Cyndaquil.heal()
# Charmander.attacks(Cyndaquil)
# Cyndaquil.attacks(Charmander)


# #this is us playing around to see if I understand it
# class A:
#     b = 20
#     def __init__(self, a):
#         self.a = a

#     def the_third(self):
#         return self.a ** 3

#     def __add__(self, other):
#         return self.a + other.a


# obj1 = A(5)
# obj2 = A(10)
# print(obj1 + obj2)  # 15
# #print(obj1 - obj2)

# print(obj1.the_third())

# obj3 = A(20)
# print(obj3.a, obj3.b)
