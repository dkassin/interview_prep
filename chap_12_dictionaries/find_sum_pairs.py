class FindSumPairs:
    def __init__(self, nums1, nums2):
        self.nums1, self.nums2 = nums1,nums2

    def add(self, index,val):
        self.nums2[index] += val

    def count(self,tot):
        track_hash = {}
        for index,value in enumerate(self.nums1):
            target = tot - value
            if target not in track_hash:
                track_hash[target] = track_hash.get(target, 0) + 1
            else:
                track_hash[target].add(index)
        count = 0
        for index, value in enumerate(self.nums2):
            if value in track_hash:
                nums_1_count = len(track_hash[value])
                count += (nums_1_count)
        return count
    
## Improved but still to slow

class FindSumPairs:
    def __init__(self, nums1, nums2):
        self.nums1, self.nums2 = nums1,nums2

    def add(self, index,val):
        self.nums2[index] += val

    def count(self,tot):
        track_hash = {}
        for num in self.nums1:
            target = tot - value
            track_hash[num].get(num,0) + 1
        count = 0
        for num in self.nums2:
            count += track_hash.get(num,0)
        return count
    