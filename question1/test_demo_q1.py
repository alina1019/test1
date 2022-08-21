import random

from question1 import sort_function

random_list = random.sample(range(0, 100), 10)
print("Initial sequence:", random_list)
print("Sorted sequence:", sort_function(random_list))

