import random
from random import randint

x = random.sample(range(0, 100), randint(0, 50))
y = random.sample(range(0, 100), randint(0, 50))

lst = list(set(x).intersection(y))

print(lst)
