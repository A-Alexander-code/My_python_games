import readchar
from random import randint, random
import os 

pos_x = 0
pos_y = 1
number_of_map_objects = 11

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
tail_lenght = 0
tail = []
map_objects = []

end_game = False
died = False

# Create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
map_width = len(obstacle_definition[0])
map_height = len(obstacle_definition)


# Main loop
while not end_game:
    os.system("cls")
    
    # Generate random onjects on the map
    while len(map_objects) < number_of_map_objects:
        new_position = [randint(0, map_width - 1), randint(0, map_height - 1)]
        
        if new_position not in map_objects and new_position != my_position and \
            obstacle_definition[new_position[pos_y]][new_position[pos_x]] != "#":
            map_objects.append(new_position)

    #Draw Map (borders)
    print("+" + "-"*(map_width*3) + "+")

    for coordinate_y in range(map_height):
        print("|", end="")
        
        for cordinate_x in range(map_width):
            
            char_to_draw = "   "
            object_in_cell = None
            tail_in_cell = None
            
            for mobject in map_objects:
                if mobject[pos_x] == cordinate_x and mobject[pos_y] == coordinate_y:
                    char_to_draw = "¿*?"
                    object_in_cell = mobject
            
            for tail_piece in tail:
                if tail_piece[pos_x] == cordinate_x and tail_piece[pos_y] == coordinate_y:
                    char_to_draw = "=@="
                    tail_in_cell = tail_piece
            
            if my_position[pos_x] == cordinate_x and my_position[pos_y] == coordinate_y:
                char_to_draw = "ºwº"
                
                if object_in_cell:
                    map_objects.remove(object_in_cell)
                    tail_lenght += 1
                
                if tail_in_cell:
                    end_game = True
                    died = True
            
            if obstacle_definition[coordinate_y][cordinate_x] == "#":
                char_to_draw = "[#]"
            
            print("{}".format(char_to_draw), end="")
        print("|")

    print("+" + "-"*(map_width*3) + "+")
    print("Tail lenght {}".format(tail_lenght))
    #print("Tail position {}".format(tail))

    # Ask user where he/she wants to move
    #direction = input("Where do you want to move? [WASD]\n")
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
            tail.insert(0, my_position.copy())
            tail = tail[:tail_lenght]
            my_position = new_position

if died == True:
    print("You died!")