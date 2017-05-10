import random
from random import randint

lst = random.sample(range(0, 100), randint(0, 50))
lst = list(filter(lambda x: x % 2 == 0, lst))

print(lst)
