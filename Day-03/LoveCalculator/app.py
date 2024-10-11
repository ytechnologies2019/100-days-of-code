import random

print ("Welcome to Love Calculator")
name1 = input("Add the first person name : ")
name2 = input("Add the second person name : ")
love_percent = random.randint(0,100)

if love_percent >= 0 and love_percent < 40:
    print (f"Your Love percentage is {love_percent} and not true")
elif love_percent >= 40 and love_percent < 70:
    print (f"Your Love percentage is {love_percent} and I guess you love each other")
else:
    print (f"Your Love percentage is {love_percent} and amazing love")