class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        left = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in unique:
                unique.remove(s[left])
                left += 1
            unique.add(s[r])
            longest = max(longest, r - left + 1)
        return longest