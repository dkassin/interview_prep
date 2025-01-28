def is_derangement(arr1, arr2):
    count = min(len(arr1),len(arr2))
    for i in range(0,count):
        if arr1[i] == arr2[i]:
            return False
    return True    

arr1, arr2 = [1,2,3,5],[5,2,1,4]
arr3, arr4 = [1,2,4,5],[7,8,9,10]
print(is_derangement(arr1, arr2))
print(is_derangement(arr3, arr4))