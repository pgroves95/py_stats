def mode(num_list):

    mode_counter = {}
    highest_recurrence = 1
    mode_list = []

    for num in num_list:
        if num in mode_counter.keys():
            mode_counter[num] += 1
        else:
            mode_counter[num] = 1

    for count in mode_counter.values():
        if count > highest_recurrence:
            highest_recurrence = count

    if highest_recurrence == 1:
        return None

    for key in mode_counter.keys():
        if mode_counter[key] == highest_recurrence:
            mode_list.append(key)
    return mode_list


print(mode([11, 22, 33, 44, 55, 66, 66, 33, 33, 33]))
