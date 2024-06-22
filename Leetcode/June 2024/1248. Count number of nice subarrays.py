from collections import Counter

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_count = Counter({0: 1})
        answer = temp_odd_count = 0
        for value in nums:
            temp_odd_count += value & 1 
            answer += odd_count[temp_odd_count - k]
            odd_count[temp_odd_count] += 1
      
        return answer
