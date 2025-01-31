def merge_sorted_lists(list1,list2):
    array = []
    while list1 and list2:
        if list1[0] <= list2[0]:
            temp = list1.pop(0)
            array.append(temp)
        else:
            temp = list2.pop(0)
            array.append(temp)
        
    if len(list1) == 0:
        array.extend(list2)
    else: array.extend(list1)
     
    return array   

list1 = [1,5,8,12]
list2 = [0,1,4,7]
assert merge_sorted_lists(list1, list2) == [0,1,1,4,5,7,8,12]
