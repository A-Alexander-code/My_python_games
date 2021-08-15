from random import randint
import os

# pikachu -> pk
# squirtle -> sqt
# i -> initial
# ac -> actual
# lf -> life
# pct -> percent base 1
# attack -> atk

pk_ilf = 80
sqt_ilf = 90
lf_bar = 20

pk_lf = pk_ilf
sqt_lf = sqt_ilf


while pk_lf > 0 and sqt_lf > 0:

    # Se desenvuelven los turnos

    # Turno de pikachu
    print("Pikachu's turn")
    pk_atk = randint(1, 3)
    if pk_atk == 1:
        print("Pikachu chooses voltio ball")
        sqt_lf -= 10
    elif pk_atk == 2:
        print("Pikachu attacks with thunder wave")
        sqt_lf -= 11
    else:
        print("Pikachu's attack failed")
    
    pk_pct_lf = pk_lf / pk_ilf
    sqt_pct_lf = sqt_lf / sqt_ilf
    
    print("Pikachu's life is: [{}] - {}%".format("*"*round(lf_bar * pk_pct_lf), round((100*pk_pct_lf), 1)))
    print("Squirtle's life is: [{}] - {}%".format("*"*round(lf_bar * sqt_pct_lf), round((100*sqt_pct_lf), 1)))
    
    input("Press enter to continue")
    
    os.system("cls")

    # Turno de squirtle
    print("Squirtle's turn")
    sqt_atk = None
    while sqt_atk != "P" and sqt_atk != "W" and sqt_atk != "B" and sqt_atk != "N":
        sqt_atk = input("¿What attack do you choose? \n"
                        "[P] Strong punch\n"
                        "[W] Water pistol\n"
                        "[B] Bubbles\n"
                        "[N] Do nothing \n")

    if sqt_atk == "P":
        print("Squirtle uses strong punch")
        pk_lf -= 10
    elif sqt_atk == "W":
        print("Squirtle uses water pistol")
        pk_lf -= 12
    elif sqt_atk == "B":
        print("Squirtle uses bubbles")
        pk_lf -= 9
    else:
        print("Squirtle's attack failed ")

    pk_pct_lf = pk_lf / pk_ilf
    sqt_pct_lf = sqt_lf / sqt_ilf
    
    print("Pikachu's life is: [{}] - {}%".format("*"*round(lf_bar * pk_pct_lf), round((100*pk_pct_lf), 1)))
    print("Squirtle's life is: [{}] - {}%".format("*"*round(lf_bar * sqt_pct_lf), round((100*sqt_pct_lf), 1)))
    
    input("Press enter to continue")
    
    os.system("cls")

if pk_lf < 0:
    pk_lf = 0

if sqt_lf < 0:
    sqt_lf = 0

if pk_lf > sqt_lf:
    print("Pikachu wins!")
else:
    print("Squirtle wins!")