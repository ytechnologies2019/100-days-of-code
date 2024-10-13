import random
import module
##Return Random Number
random_int = random.randint(1,100)
##Return the Float Number -> 0-1
random_float = random.random()
print (random_float)
##Return 0 to 5
random_float_5 = random.random() * 5
print (random_float_5)

print(random_int)
print (f"Came from the module.py file : {module.module_num}")