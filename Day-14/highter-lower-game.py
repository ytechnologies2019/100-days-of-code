import art
import gamedata
import random

def guess():

    print(art.logo)


    score = 0
    count = 3
    while count > 0:
        random_data1 = random.choice(gamedata.data)
        random_data2 = random.choice(gamedata.data)
        name1 = random_data1.get('name')
        name2 = random_data2.get('name')

        print(f"{name1} {art.vs} {name2}")

        score1 = random_data1.get('follower_count')
        score2 = random_data2.get('follower_count')
        user_input = int(input("Choose 1 or 2 : "))

        if user_input not in [1 , 2]:
            print ("Please Choose 1 and 2")
            continue

        if user_input == 1:
            print (name1)
            #Compare Score
            if score1 > score2:
                print ("You Won")
                score += 1
                print (score)
            else:
                print ("You Lose")

        if user_input == 2:
            print (name2)
            if score2 > score1:
                print ("You Won")
                score += 1
                print (score)
            else:
                print ("You Lose")

        count -= 1
    print(f"Your Total Score is: {score}")
guess()