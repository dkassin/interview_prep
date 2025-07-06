## This works but is not optimal but does pass

from collections import Counter
def check_inclusion(s1,s2):
    start = 0
    s1_check = Counter(s1)
    for end in range(len(s2)):

        if end - start +1 == len(s1):
            if Counter(s2[start:end+1]) == s1_check:
                return True
            else:
                start += 1
    return False

### Here is a better version

def check_inclusion(s1,s2):
    if len(s1) > len(s2):
        return False
    
    start = 0
    s1_check = Counter(s1)
    s2_check = Counter()

    for end in range(len(s2)):
        s2_check[s2[end]] += 1
        if end - start +1 > len(s1):
            s2_check[start] -= 1
            if s2_check[start] == 0:
                del s2_check[start]
            start += 1
        
        if s2_check == s1_check:
            return True
    return False