class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = []
        left = []

        prev = 1
        for i in range(len(nums)):
            if i == 0:
                left.append(prev)
            else:
                left.append(prev * nums[i-1])
                prev = prev * nums[i-1]

        prev = 1
        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 1:
                right.append(1)
            else:
                right.append(prev * nums[j + 1])
                prev = prev * nums[j + 1]

        
        right.reverse()
        output = []
        for k in range(len(nums)):
            output.append(right[k] * left[k])

        return output
            