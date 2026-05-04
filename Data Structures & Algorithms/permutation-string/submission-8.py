class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_count = {}
        window_count = {}

        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1
        
        l, r = 0, len(s1) - 1

        for i in range(l, r + 1):
            c = s2[i]
            window_count[c] = window_count.get(c, 0) + 1

        while r < len(s2) - 1:
            if window_count == s1_count:
                return True
        
            window_count[s2[l]] -= 1
            if window_count[s2[l]] == 0:
                del window_count[s2[l]]

            l += 1
            r += 1

            window_count[s2[r]] = window_count.get(s2[r], 0) + 1

        return window_count == s1_count