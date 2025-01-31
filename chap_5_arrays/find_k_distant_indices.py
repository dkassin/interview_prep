def find_k_distant_indices(nums,key,k):
    k_index = []
    distant_index = set()
    for index, value in enumerate(nums):
        if value == key:
            k_index.append(index)

    for index, _ in enumerate(nums):
        for j in k_index:
            if abs(index - j) <= k:
                distant_index.add(index)
                
    return [i for i in distant_index]

assert find_k_distant_indices([3,4,9,1,3,9,5],9,1) == [1,2,3,4,5,6]
assert find_k_distant_indices([2,2,2,2,2],2,2) == [0,1,2,3,4]

