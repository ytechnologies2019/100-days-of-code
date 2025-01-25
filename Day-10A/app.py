import random
print ("🍩🐳🇬​🇺​🇪​🇸​🇸​ 🇹​🇭​🇪​ 🇳​🇺​🇲​🇧​🇪​🇷​😲")
random_number = random.randint(3, 100)
print (random_number)
user_input = input("Choose your level easy or hard :")

if user_input == "easy":

    def easy():
        print ("You will get 10 chances")
        try_count = 10

        while try_count > 0:
            user_choose = int(input("Choose your number :"))
            if user_choose < random_number:
                print ("Less than the result")
            elif user_choose > random_number:
                print ("Greater than the result")
            else:
                print ("𝕐𝕠𝕦 𝕨𝕠𝕟 𝕥𝕙𝕖 𝕘𝕒𝕞𝕖!")
                break
            try_count -= 1
            print(f"You have {try_count} remaining")
            if try_count == 0:
                print(f"🅖🅐🅜🅔 🅞🅥🅔🅡")
                print(f"The right number is {random_number}")
    easy()

elif user_input == "hard":
    def hard():
        print ("You will get 5 chances")
        try_count = 5

        while try_count > 0:
            user_choose = int(input("Choose your number :"))
            if user_choose < random_number:
                print ("Less than the result")
            elif user_choose > random_number:
                print ("Greater than the result")
            else:
                print ("𝕐𝕠𝕦 𝕨𝕠𝕟 𝕥𝕙𝕖 𝕘𝕒𝕞𝕖!")
                break
            try_count -= 1
            print (f"Your have {try_count} remaining")
            if try_count == 0:
                print(f"🅖🅐🅜🅔 🅞🅥🅔🅡")
                print(f"The right answer is {random_number}")

    hard()

else:
    print ("You chose wrong!")