from shlex import join

from question3 import get_next_permutation

input1 = list("1234")
c = get_next_permutation(input1)
print(join(c))

