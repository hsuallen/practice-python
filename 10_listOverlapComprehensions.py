import random
from random import randint

x = random.sample(range(0, 100), randint(0, 50))
y = random.sample(range(0, 100), randint(0, 50))

if (len(x) <= len(y)):
    print([n for n in x if n in y])
else:
    print([n for n in y if n in x])
