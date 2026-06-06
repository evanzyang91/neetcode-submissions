class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        biggest = float('-inf')
        curr = float('-inf')
        for n in nums:
            curr = max(n, curr + n)
            biggest = max(biggest, curr)
        return biggest