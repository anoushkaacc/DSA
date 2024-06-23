from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        max_deque = deque()
        min_deque = deque()
        longest = 0

        for right in range(len(nums)):
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()

            max_deque.append(right)
            min_deque.append(right)

            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()

            longest = max(longest, right - left + 1)     

        return longest                  



# sliding window logic -
## Iterate over the array with a right pointer right.
##Maintain the max_deque and min_deque to always store indices in decreasing and increasing order of the corresponding elements in nums.
##If the difference between the maximum and minimum values in the current window exceeds the limit, move the left pointer to shrink the window until the difference is within the limit.
##Update the longest with the length of the current valid window.
