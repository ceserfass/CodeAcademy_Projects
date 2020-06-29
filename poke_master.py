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

    def health_check(self):
        if self.current_health < 0:
            self.current_health = 0
        if self.current_health > 100:
            self.current_health = 100
        return self.current_health

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

    def use_potion(self, target_pokemon, potion=None):

        if potion == None:
            if self.potions[0] != None:
                target_pokemon.heal(100)
                print(f'Used {self.potions[0]}.')
                self.potions.pop(0)
                
        else:
            index_count = 0
            for i in self.potions:
                if i == potion:
                    target_pokemon.heal(100)
                    print(f'Used {potion}.')
                    self.potions.pop(index_count)
                    return
                index_count += 1
            return print(f"{potion} is not in your inventory.")   


            # chceck if potion is in the potion list
            #error handling
            # if it is, use it

    def switch_pokemon(self, new_pokemon):
        # this is going to work for both yourself and the opposing trainer

        if self.current_pokemon == new_pokemon:
            return print('Already current!')

        for i in self.pokemon:

            if new_pokemon.name == i.name:
                if i.awake == True:
                    self.current_pokemon = i
                    return print(f"Switched current pokemon to {i.name}")

                return print(f"{i.name} is Unconcious. Choose another!")


        return print("Pokemon not owned! Better catch 'em all!")


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
Charmander = Pokemon("Charmander", 60, "Fire", awake_asleep=False)
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
# print(Ash)
# Ash.use_potion(Charmander, "antidote")
# print(Ash)



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

# HOW TO WORK COLLABORATIVELY IN GIT / GITHUB
# Fetch and merge changes from the remote
#     Create a branch to work on a new project feature
#     Develop the feature on your branch and commit your work
#     Fetch and merge from the remote again (in case new commits were made while you were working)
#     Push your branch up to the remote for review
