from traceback import print_tb

print("Welcome to TreasureGame")
hole=input("Choose turn right or left? R or L :")

if hole == "R" or hole == "r":
    print ("Fallen to the Hole and Game Over!")
elif hole == "L" or hole == "l":
    swim = input("Swim or Wait?"" S or W :")
    if swim == "S" or swim == "s":
        print ("Game Over")
    elif swim == "W" or swim == "w":
        door = input("Which Door? Red or Green or Blue? R or G or B :")
        if door == "R" or  door == "r" or door == "G" or door == "g":
            print ("Game Over")
        elif door == "B" or "b":
            print ("You Win!")
        else:
            print (f"{hole} option is not working for this game")
