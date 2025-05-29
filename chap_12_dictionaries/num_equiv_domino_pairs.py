from collections import defaultdict
from math import comb

def num_equiv_domino_pairs(dominoes) -> int:
    default = defaultdict(int)
    for i in dominoes:
        min_val = min(i[0],i[1])
        max_val = max(i[0],i[1])
        default[(min_val,max_val)] += 1

    result = 0
    for val in default.values():
        result += val * (val - 1) // 2
        # Can also use math import comb
        ## result += math.comb(val,2)
    return result

assert num_equiv_domino_pairs([[1,2],[2,1],[3,4],[5,6]]) == 1
assert num_equiv_domino_pairs([[1,2],[1,2],[1,1],[1,2],[2,2]]) == 3
