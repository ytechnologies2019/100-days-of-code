fruits = eval(input())
# 🚨 Do not change the code above

# TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):

    try:
        fruit = fruits[index]

    except NameError:
        print(fruit + " pie")

    else:
        print ("Welcome to Fruit World")

# 🚨 Do not change the code below
make_pie(4)
