class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freqs = {}
        for char in t:
            freqs[char] = freqs.get(char, 0) + 1

        cfreqs = {}
        substrings = {}

        l = 0
        needs = len(freqs) 
        haves = 0

        for r in range(len(s)):
            char = s[r]

            # expand window
            if char in freqs:
                cfreqs[char] = cfreqs.get(char, 0) + 1

                if cfreqs[char] == freqs[char]:
                    haves += 1

            # shrink window
            while haves == needs:
                substrings[s[l:r+1]] = r - l + 1

                left_char = s[l]
                if left_char in freqs:
                    cfreqs[left_char] -= 1

                    if cfreqs[left_char] < freqs[left_char]:
                        haves -= 1

                l += 1

        if substrings:
            shortest = min(substrings, key=substrings.get)
            return shortest
        else:
            return ""