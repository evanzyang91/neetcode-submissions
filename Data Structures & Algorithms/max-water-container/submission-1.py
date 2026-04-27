class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        left = 0 
        right = len(heights) - 1
        while left < right:
            if min(heights[left], heights[right]) * abs(left - right) > maximum:
                maximum = min(heights[left], heights[right]) * abs(left - right)

            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1 
            else:
                left += 1 
                right -= 1
        return maximum