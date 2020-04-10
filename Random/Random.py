from random import seed
from random import randint

seed(1)

for _ in range(10):
	value = randint(0, 10)
	print(value)