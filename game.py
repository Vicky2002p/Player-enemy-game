# game.py
from player import player
from enemy import enemy

#Game class
class game:
    round = 1
    def play(self):
        #creates a player object 
        #repeatedly creates new enemy object
        #until the player's health falls to 0 or below.
        player1 = player()
        enemy1 = enemy()
        while(player1.is_alive() and enemy1.is_alive()):
            print("Player", player1.health)
            print("Enemy", enemy1.health)
            if enemy1.health < 50:
                enemy1.new_enemy(enemy1)
            enemy1.attack(player1)
            player1.attack(enemy1)
            player1.heal()  
            
            print(game.round)
            game.round += 1
        if player1.is_alive():
            print("player wins")
        else: 
            print("enemy wins")

game1 = game()
game1.play()












# class player:
#     player_num = 1
#     health_P = 100
#     def attack(self):
#         if enemy.health_E > 0:
#             enemy.health_E = enemy.health_E - 50
#             print(enemy.health_E)
#             return enemy.attack(self)
#         else:
#             print("player wins")
# class enemy:
#     enemy_num = 1
#     health_E = 100
#     def attack(self):
#         if player.health_P > 0:
#             player.health_P = player.health_P - 50
#             print(player.health_P)
#             return player.attack(self)
#         else:
#             print("enemy wins")

# attacker = player()
# print(attacker.attack())