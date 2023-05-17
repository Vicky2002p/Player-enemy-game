# enemy.py
import random
from Character import character

# Enemy class inherits from the character class
class enemy(character):
    def new_enemy(self, enemy):
        #generates a new enemy object with random health value
        amount = random.randint(30,100)
        enemy.health = amount

# enem = enemy()
# enem.new_enemy
# print(enem.numEnemy)  