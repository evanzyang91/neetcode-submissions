from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = defaultdict(int)
        l = 0
        longest = 0
        maxf = 0

        for r in range(len(s)):
            freqs[s[r]] += 1
            maxf = max(maxf, freqs[s[r]])

            while r - l - maxf + 1 > k:
                freqs[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)

        return longest