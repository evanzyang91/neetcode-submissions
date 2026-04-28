class Solution:
    def trap(self, height: List[int]) -> int:
        rmax = [0] * len(height)
        lmax = [0] * len(height)

        tempMax = 0
        for h in range(len(height)):
            if h > 0:
                tempMax = max(tempMax, height[h-1])
            lmax[h] = tempMax

        tempMax = 0
        for h in range(len(height) - 1, -1, -1):
            if h < len(height) - 1:
                tempMax = max(tempMax, height[h+1])
            rmax[h] = tempMax

        total = 0
        for i in range(len(height)):
            total += max(0, min(lmax[i], rmax[i]) - height[i])

        return total