# Requires sorted list

def median(num_list):
    sorted_num_list = sorted(num_list)
    middle_position = len(sorted_num_list) // 2

    if len(sorted_num_list) % 2 == 1:
        return sorted_num_list[middle_position]

    even_median_sum = sorted_num_list[middle_position] + \
        sorted_num_list[middle_position - 1]
    even_median = even_median_sum / 2
    return even_median


# test cases
print(median([2, 2, 3, 3]))
print(median([1, 2, 3, 4, 5]))
print(median([2, 3, 4, 5, 6, 9, 12]))
print(median([77, 33, 33, 66, 99, 108]))
