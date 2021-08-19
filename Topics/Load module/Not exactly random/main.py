from random import randint
from random import seed

n = int(input())
seed(n)
print(randint(-100, 100))
