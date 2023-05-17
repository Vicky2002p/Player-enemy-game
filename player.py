# player.py
from Character import character

# Player class inherits from the character class
class player(character):
    # def __init__(self, health):
    #     self.health = health
    def heal(self, amount=10):
        #increases health by certain amount
        self.health += amount

# Play = player()
# Play.heal()
# print(Play.health)
