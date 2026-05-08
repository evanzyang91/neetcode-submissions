class Solution:
    def isValid(self, s: str) -> bool:
        L = len(s)
        if L % 2 != 0:
            return False

        valids = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        
        stack = []
        for b in s:
            if b in valids:
                stack.append(b)
            elif (len(stack) == 0) or (b != valids[stack.pop()]):
                return False
        if len(stack) != 0:
            return False
        return True
                
        