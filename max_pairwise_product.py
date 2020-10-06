def max_pairwise_product(numbers):
    max_number = 0
    n = len(numbers)
    for first in range(n):
        for second in range(first + 1, n):
            max_number = max(max_number, numbers[first] * numbers[second])
    return max_number

input_numbers = [int(x) for x in raw_input("Enter multiple value: ").split()]
print "Max pairwise product equals:: %d" % max_pairwise_product(input_numbers)
    