print ("Welcome to RollerCoaster!")
height = float(input("Enter Your height: \n"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = float(input("Enter Your Age: \n"))

    if age >= 18:
        photo = (input("If you wanna take photo , please type Y \n"))
        if photo == "Y" or "y" :
           photo_bill = 3
           rollercoaster_bill = 12
           print(f"Total bill is {rollercoaster_bill + photo_bill}  " )
        else:
           print(f"Total bill is $12")
    else:
        print ("You need to pay $7")
else:
    print ("Sorry , you've to grow before you can ride")
