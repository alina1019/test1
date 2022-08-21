def sort_function(array):

    for i in range(1, len(array)):
        position = i
        value = array[i]

        while position > 0 and array[position-1] > value:
            array[position] = array[position-1]
            position = position-1

        array[position] = value
    return array

# Complexity of the algorithm:
# O(n^2) runtime complexity - average /worst case
# O(n) runtime complexity - best case



