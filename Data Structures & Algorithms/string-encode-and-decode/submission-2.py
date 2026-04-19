class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string = ""
        for item in strs:
            encoded_string += str(len(item)) + "#" + item

        return encoded_string

    def decode(self, s: str) -> List[str]:

        output = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word = s[j+1:j+length+1]
            output.append(word)
            i = j + length + 1
        
        return output