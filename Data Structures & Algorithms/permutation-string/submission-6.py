from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqs = defaultdict(int)
        for char in s1:
            freqs[char] += 1
        
        l = 0
        curr = defaultdict(int)

        for r in range(len(s2)):
            char = s2[r]

            if char not in freqs:
                curr.clear()
                l = r + 1
                continue

            curr[char] += 1

            while curr[char] > freqs[char]:
                curr[s2[l]] -= 1
                l += 1

            if r - l + 1 == len(s1):
                return True

        return False