import readchar
from random import randint, random
import os 

# Pokemon information
pokemon_list = ["Bulbasaur", "Charmander", "Squirtle", "Pidgey", "Ekans", "Mankey"]
pokemon_life = [135, 127, 140, 150, 130, 145]
# Bulbasaur data sheet
blb_moves = ["Growl", "Tackle", "Vine whip", "Heal"]
blb_atk = [17, 22, 15, 10]
# Charmander data sheet
chr_moves = ["Flametower", "Scary face", "Fire spin", "Inferno"]
chr_atk = [18, 13, 15, 20]
# Squirtle data sheet
sqt_moves = ["Tail whip", "Water gun", "Withdraw", "Rapid spin"]
sqt_atk = [16, 18, 20, 13]
# Pidgey data sheet
pdg_moves = ["Gust", "Quick attack", "Whirlwind", "Heal"]
pdg_atk = [13, 23, 10, 15]
# Ekans data sheet
ek_moves = ["Poison jab", "Slam", "Screech", "Toxic"]
ek_atk = [17, 13, 18, 21]
# Mankey data sheet
mky_moves = ["Karate chop", "Fury swipes", "Low kick", "Seismic toss"]
mky_atk = [20, 15, 10, 13]

print("Welcome triner to the jungle!! Defeat the rest of the trainers to win.")

print("Choose your partner.")
for i in range(len(pokemon_list)):
    print(i+1, pokemon_list[i])
player_choose = int(input())


if player_choose == 1:
    pk_partner = pokemon_list[0]
    pk_partner_life = pokemon_life[0]
    pk_moves = blb_moves
    pk_atk = blb_atk
    
elif player_choose == 2:
    pk_partner = pokemon_list[1]
    pk_partner_life = pokemon_life[1]
    pk_moves = chr_moves
    pk_atk = chr_atk

elif player_choose == 3:
    pk_partner = pokemon_list[2]
    pk_partner_life = pokemon_life[2]
    pk_moves = sqt_moves
    pk_atk = sqt_atk

elif player_choose == 4:
    pk_partner = pokemon_list[3]
    pk_partner_life = pokemon_life[3]
    pk_moves = pdg_moves
    pk_atk = pdg_atk

elif player_choose == 5:
    pk_partner = pokemon_list[4]
    pk_partner_life = pokemon_life[4]
    pk_moves = ek_moves
    pk_atk = ek_atk

else:
    pk_partner = pokemon_list[5]
    pk_partner_life = pokemon_life[5]
    pk_moves = mky_moves
    pk_atk = mky_atk

# New pokemon list with enemies
pk_enemies = []
for i in pokemon_list:
    if i != pk_partner:
        pk_enemies.append(i)

pk_enemies_life = []
for i in pokemon_life:
    if i != pk_partner_life:
        pk_enemies_life.append(i)

print("\nYou had choosen {} as your partner.".format(pk_partner))
print("Its life is {} HP".format(pk_partner_life))
print("Its special moves are: ", pk_moves)
print(pk_atk)
#print(pk_enemies)
#print(pk_enemies_life)
input("Press enter to continue...")
os.system("cls")

# Enemies order
enemy_order = []

while len(enemy_order) != len(pk_enemies):
    enemy_id = randint(0, len(pk_enemies)-1)
    if pk_enemies[enemy_id] not in enemy_order:
        enemy_order.append(pk_enemies[enemy_id])

#print(enemy_order)

pos_x = 0
pos_y = 1
pk_trainer = 5
pk_trainer_defeat = 0

obstacle_definition = """\
####      ####  #####     ###
####      ####  #####        
          ####               
######    ####    ###        
######    ####    ###     ###
######    ####    ###     ###
     #    ####    ###        
     #    ####    ###     ###
                             
   #####    ###########   ###
   #####    ##                             
   #####    ##   ######   ###
########    ##      ###   ###
            ##      ###      \
"""

my_position = [6, 3]
map_trainer = []

end_game = False
died = False
player_life = False

# Create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
map_width = len(obstacle_definition[0])
map_height = len(obstacle_definition)

# Generate random onjects on the map
while len(map_trainer) < pk_trainer:
    new_position = [randint(0, map_width - 1), randint(0, map_height - 1)]
        
    if new_position not in map_trainer and new_position != my_position and \
        obstacle_definition[new_position[pos_y]][new_position[pos_x]] != "#":
        map_trainer.append(new_position)

# Main loop
while not end_game and not player_life:
    
    # Pokemon partner attacks
    atk_01 = pk_atk[0]
    atk_02 = pk_atk[1]
    atk_03 = pk_atk[2]
    atk_04 = pk_atk[3]
    
    
    lf_bar = 20
    
    # Pokemon partner life
    pok_player  = pk_partner
    pok_player_ilife = pk_partner_life
    pok_player_life = pok_player_ilife
    
    # Pokemon enemies 
    pc_pokemon = enemy_order
    
    if pc_pokemon[0] == "Bulbasaur":
        pok_pc = pokemon_list[0]
        pok_pc_ilife = pokemon_life[0]
        pok_pc_life = pok_pc_ilife
        pc_mov01, pc_atk01 = blb_moves[0], blb_atk[0]
        pc_mov02, pc_atk02 = blb_moves[1], blb_atk[1]
        pc_mov03, pc_atk03 = blb_moves[2], blb_atk[2]
        pc_mov04, pc_atk04 = blb_moves[3], blb_atk[3]
    elif pc_pokemon[0] == "Charmander":
        pok_pc = pokemon_list[1]
        pok_pc_ilife = pokemon_life[1]
        pok_pc_life = pok_pc_ilife
        pc_mov01, pc_atk01 = chr_moves[0], chr_atk[0]
        pc_mov02, pc_atk02 = chr_moves[1], chr_atk[1]
        pc_mov03, pc_atk03 = chr_moves[2], chr_atk[2]
        pc_mov04, pc_atk04 = chr_moves[3], chr_atk[3]
    elif pc_pokemon[0] == "Squirtle":
        pok_pc = pokemon_list[2]
        pok_pc_ilife = pokemon_life[2]
        pok_pc_life = pok_pc_ilife
        pc_mov01, pc_atk01 = sqt_moves[0], sqt_atk[0]
        pc_mov02, pc_atk02 = sqt_moves[1], sqt_atk[1]
        pc_mov03, pc_atk03 = sqt_moves[2], sqt_atk[2]
        pc_mov04, pc_atk04 = sqt_moves[3], sqt_atk[3]
    elif pc_pokemon[0] == "Pidgey":
        pok_pc = pokemon_list[3]
        pok_pc_ilife = pokemon_life[3]
        pok_pc_life = pok_pc_ilife
        pc_mov01, pc_atk01 = pdg_moves[0], pdg_atk[0]
        pc_mov02, pc_atk02 = pdg_moves[1], pdg_atk[1]
        pc_mov03, pc_atk03 = pdg_moves[2], pdg_atk[2]
        pc_mov04, pc_atk04 = pdg_moves[3], pdg_atk[3]
    elif pc_pokemon[0] == "Ekans":
        pok_pc = pokemon_list[4]
        pok_pc_ilife = pokemon_life[4]
        pok_pc_life = pok_pc_ilife
        pc_mov01, pc_atk01 = ek_moves[0], ek_atk[0]
        pc_mov02, pc_atk02 = ek_moves[1], ek_atk[1]
        pc_mov03, pc_atk03 = ek_moves[2], ek_atk[2]
        pc_mov04, pc_atk04 = ek_moves[3], ek_atk[3]
    else:
        pok_pc = pokemon_list[5]
        pok_pc_ilife = pokemon_life[5]
        pok_pc_life = pok_pc_ilife
        pc_mov01, pc_atk01 = mky_moves[0], mky_atk[0]
        pc_mov02, pc_atk02 = mky_moves[1], mky_atk[1]
        pc_mov03, pc_atk03 = mky_moves[2], mky_atk[2]
        pc_mov04, pc_atk04 = mky_moves[3], mky_atk[3]
    
    os.system("cls")

    #Draw Map (borders)
    print("+" + "-"*(map_width*3) + "+")

    for coordinate_y in range(map_height):
        print("|", end="")
        
        for cordinate_x in range(map_width):
            
            char_to_draw = "   "
            object_in_cell = None
            
            for mobject in map_trainer:
                if mobject[pos_x] == cordinate_x and mobject[pos_y] == coordinate_y:
                    char_to_draw = "o_0"
                    object_in_cell = mobject
            
            if my_position[pos_x] == cordinate_x and my_position[pos_y] == coordinate_y:
                char_to_draw = "ºûº"
                
                if object_in_cell:
                    
                    while pok_pc_life > 0 and pok_player_life > 0:  
                        # Turns lets begin
                        # Enemies turn (pikachu)
                        print("{}'s turn".format(pok_pc))
                        pok_pc_atk = randint(1, 5)
                        if pok_pc_atk == 1:
                            print("{} chooses {} [{}]".format(pok_pc, pc_mov01, pc_atk01))
                            pok_player_life -= pc_atk01
                        elif pok_pc_atk == 2:
                            print("{} chooses {} [{}]".format(pok_pc, pc_mov02, pc_atk02))
                            pok_player_life -= pc_atk02
                        elif pok_pc_atk == 3:
                            print("{} chooses {} [{}]".format(pok_pc, pc_mov03, pc_atk03))
                            pok_player_life -= pc_atk03
                        elif pok_pc_atk == 4:
                            print("{}'s attack failded']".format(pok_pc))
                        else:
                            if pc_mov04 == "Heal":
                                print("{} chooses {} [{}]".format(pok_pc, pc_mov04, pc_atk04))
                                pok_pc_life += pc_atk04
                            else:
                                print("{} chooses {} [{}]".format(pok_pc, pc_mov04, pc_atk04))
                                pok_player_life -= pc_atk04
                        
                        pc_pct_lf = pok_pc_life / pok_pc_ilife
                        player_pct_lf = pok_player_life / pok_player_ilife
                        
                        print("{}'s life is: [{}] - {}%".format(pok_pc, "*"*round(lf_bar * pc_pct_lf), round((100*pc_pct_lf), 1)))
                        print("{}'s life is: [{}] - {}%".format(pok_player,"*"*round(lf_bar * player_pct_lf), round((100*player_pct_lf), 1)))
                        
                        input("Press enter to continue")
                        
                        os.system("cls")

                        # Player's turn
                        
                        print("{}'s turn".format(pok_player))
                        player_atk = None
                        while player_atk != "i" and player_atk != "j" and player_atk != "k" and player_atk != "l":
                            player_atk = input("""¿What attack do you choose?
[i] {} [{}]
[j] {} [{}]
[k] {} [{}]
[l] {} [{}]\n""".format(pk_moves[0], atk_01, pk_moves[1], atk_02, pk_moves[2], atk_03, pk_moves[3], atk_04))

                        if player_atk == "i":
                            print("{} uses {}".format(pok_player, pk_moves[0]))
                            pok_pc_life -= atk_01
                        elif player_atk == "j":
                            print("{} uses {}".format(pok_player, pk_moves[1]))
                            pok_pc_life -= atk_02
                        elif player_atk == "k":
                            print("{} uses {}".format(pok_player, pk_moves[2]))
                            pok_pc_life -= atk_03
                        else:
                            if pk_moves[3] == "Heal":
                                pok_player_life += atk_04
                            else:
                                pok_pc_life -= atk_04
                        

                        pc_pct_lf = pok_pc_life / pok_pc_ilife
                        player_pct_lf = pok_player_life / pok_player_ilife
                        
                        print("{}'s life is: [{}] - {}%".format(pok_pc, "*"*round(lf_bar * pc_pct_lf), round((100*pc_pct_lf), 1)))
                        print("{}'s life is: [{}] - {}%".format(pok_player,"*"*round(lf_bar * player_pct_lf), round((100*player_pct_lf), 1)))
                        
                        input("Press enter to continue")
                        
                        os.system("cls")
                
                if object_in_cell:
                    if pok_pc_life < 0:
                        pok_pc_life = 0

                    if pok_player_life < 0:
                        pok_player_life = 0

                    if pok_pc_life > pok_player_life:
                        print("{} wins!".format(pok_pc))
                        player_life = True
                    else:
                        print("{} wins!".format(pk_partner))
                        pk_trainer_defeat += 1
                        map_trainer.remove(object_in_cell)
                        pc_pokemon.remove(pok_pc)
                
                if object_in_cell:
                    if pk_trainer_defeat == 5:
                        print("Congratulations!!! You are a pokemon master.")
                        end_game = True

            
            if obstacle_definition[coordinate_y][cordinate_x] == "#":
                char_to_draw = "[#]"
            
            print("{}".format(char_to_draw), end="")
        print("|")

    print("+" + "-"*(map_width*3) + "+")
    print("Enemies defeat {} of 5".format(pk_trainer_defeat))

    direction = readchar.readchar().decode()
    new_position = None

    if direction == "w":
        new_position = [my_position[pos_x], (my_position[pos_y] - 1) % map_height]
        
    elif direction == "s":
        new_position = [my_position[pos_x], (my_position[pos_y] + 1) % map_height]
        
    elif direction == "a":
        new_position = [(my_position[pos_x] - 1) % map_width, my_position[pos_y]]
        
    elif direction == "d":
        new_position = [(my_position[pos_x] + 1) % map_width, my_position[pos_y]]
        
    elif direction == "q":
        end_game = True
    
    if new_position:
        if obstacle_definition[new_position[pos_y]][new_position[pos_x]] != "#":
            my_position = new_position

if died == True:
    print("You died!")