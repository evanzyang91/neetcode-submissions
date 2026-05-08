class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if not stack:
                    return False
                elif char == ')' and stack.pop() != '(':
                    return False
                elif char == ']' and stack.pop() != '[':
                    return False
                elif char == '}' and stack.pop() != '{':
                    return False
        if stack:
            return False
        else:
            return True