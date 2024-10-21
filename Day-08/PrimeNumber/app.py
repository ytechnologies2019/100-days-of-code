def prime_checker(number):
    if number < 2:
        print("It's not a prime number")
        return
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            print("It's not a prime number")
            return
    print("It's a prime number")

# Do NOT change any of the code below👇
n = int(input())  # Check this number
prime_checker(number=n)
