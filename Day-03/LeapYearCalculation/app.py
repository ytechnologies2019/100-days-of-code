input_year = int((input("Enter the year: \n")))

if input_year % 4 == 0:
    if input_year % 100 == 0:
        if input_year % 400 == 0:
            print ("This is a leap year")
        else:
            print ("This is common year")
    else:
        print ("This is common year")

else:
    print ("This is not leap year")