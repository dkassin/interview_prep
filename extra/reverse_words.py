def reverse_words(array):
    join_strings = "".join(array)
    array_of_strings = join_strings.split(' ')
    left, right = 0,len(array_of_strings)-1
    while left <= right:
        array_of_strings[left], array_of_strings[right] = array_of_strings[right], array_of_strings[left]
        left += 1
        right -=1    
    return " ".join(array_of_strings)

message = [ 'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l' ]
reverse_words(message)
assert reverse_words(message) == 'steal pound cake'
