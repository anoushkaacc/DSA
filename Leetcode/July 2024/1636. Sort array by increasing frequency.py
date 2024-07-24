from collections import Counter
class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        frequency_map=Counter(nums)
        nums.sort(key=lambda x: (frequency_map[x], -x))
        return nums        
