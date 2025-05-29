def min_index_of_two_list(list1, list2):
    hash_2 = {}
    for j in range(len(list2)):
        hash_2[list2[j]] = j
    
    min_index = 10000000000
    result = []
    for i in range(len(list1)):
        if list1[i] in hash_2:
            value = i + hash_2[list1[i]]
            if value < min_index:
                result = [list1[i]]
                min_index = value
            elif value == min_index:
                result.append(list1[i])
    return result


assert min_index_of_two_list(["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]) == ["Shogun"]
assert min_index_of_two_list(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Shogun","Burger King"]) == ["Shogun"]
assert min_index_of_two_list(["happy","sad","good"],["sad","happy","good"]) == ["happy","sad"]
    