# Character.py

#Character class
class character:
    health = 100
    def __init__(self, health=100):
        self.health = health
    def attack(self, other):
        #takes character object as input
        #reduces the health to certain amount
        other.health -= 40
        return other.health
    
    def is_alive(self):
        #returns true if the health is greater than 0
        #false otherwise
        if self.health > 0:
            return True
        else:
            return False

# chara = character()
# print(chara.health)
# chara.attach(chara)
# print(chara.is_alive())
# print(chara.health)
# print(chara.is_alive())
# chara.attach(chara)
# print(chara.health)
# print(chara.is_alive())