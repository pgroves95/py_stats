def mean(num_list):
    sum = 0
    for num in num_list:
        sum += num
    mean = sum / len(num_list)

    return mean


# test cases
print(mean([1, 1, 1, 1]))
print(mean([1, 1, 2, 2]))
print(mean([1, 2, 3, 5]))
print(mean([20, 233, 12, 3.22]))
