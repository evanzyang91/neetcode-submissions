from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        consecutives = defaultdict(int)
        longest = 1
        count = 1
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif i > 0 and nums[i-1] == nums[i] -   1:
                count += 1
            else:
                count = 1
            if count > longest:
                longest = count
        return longest
        