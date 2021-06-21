# Requires sorted list

def median(num_list):
    middle_position = len(num_list) // 2

    if len(num_list) % 2 == 1:
        return num_list[middle_position]

    even_median_sum = num_list[middle_position] + \
        num_list[middle_position - 1]
    even_median = even_median_sum / 2
    return even_median


# test cases
print(median([2, 2, 3, 3]))
print(median([1, 2, 3, 4, 5]))
print(median([2, 3, 4, 5, 6, 9, 12]))
print(median([33, 33, 66, 77, 99, 108]))
