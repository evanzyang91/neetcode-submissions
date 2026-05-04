from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = Counter()

        have = 0
        need_matches = len(need)

        l = 0

        for r in range(len(s2)):
            char = s2[r]
            window[char] += 1

            if char in need and window[char] == need[char]:
                have += 1

            # keep window size fixed
            if r - l + 1 > len(s1):
                left_char = s2[l]
                if left_char in need and window[left_char] == need[left_char]:
                    have -= 1
                window[left_char] -= 1
                l += 1

            if have == need_matches:
                return True

        return False