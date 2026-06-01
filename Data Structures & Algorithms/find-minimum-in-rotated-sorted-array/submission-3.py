class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (right + left) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
                continue
            if nums[middle] <= nums[right]:
                right = middle
                continue
        return nums[left]