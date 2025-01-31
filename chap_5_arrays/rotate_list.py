def rotate_list(list,k):
    new_list = [0 for i in range(len(list))]
    for index, value in enumerate(list):
        new_index = (index + k) % len(list)
        new_list[new_index] = value

    return new_list


list1 = [1,2,3,4,5]
assert rotate_list(list1, 3) == [3,4,5,1,2]