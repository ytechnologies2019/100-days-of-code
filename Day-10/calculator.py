def calc():
    # Prompt user for inputs

    num1 = float(input("Enter your first number: "))
    while True:
        choose_operator = input("""Enter your operator: 
        + for addition
        - for subtraction
        * for multiplication
        / for division : """)

        num2 = float(input("Enter your second number: "))
        choose_continue = input("Do you want to continue?")

        # Perform the calculation based on the operator
        if choose_operator == "+":
            result = num1 + num2
            total = result

        elif choose_operator == "-":
            result = num1 - num2
            total = result

        elif choose_operator == "*":
            result = num1 * num2
            total = result

        elif choose_operator == "/":
            result = num1 / num2
            total = result

        else:
            print ("Sorry your entered the wrong operator")
        print (f"Result is {result}")
        num1 = result

        if choose_continue != "yes":
            print (f"Final result is {result}")
            break

calc()