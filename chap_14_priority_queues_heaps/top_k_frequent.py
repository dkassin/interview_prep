from collections import Counter
def top_k_frequent(nums, k):
    counts = Counter(nums)
    value = counts.most_common(k)
    return [common[0] for common in value]

assert top_k_frequent([1,1,1,2,2,3],2) == [1,2]
assert top_k_frequent([1],1) == [1]