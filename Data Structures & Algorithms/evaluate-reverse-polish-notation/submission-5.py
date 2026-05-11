class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if n == '+':
                temp = stack.pop()
                stack[-1] += temp
            elif n == '-':
                temp = stack.pop()
                stack[-1] -= temp
            elif n == '*':
                temp = stack.pop()
                stack[-1] *= temp
            elif n == '/':
                temp = stack.pop()
                stack[-1] = int(stack[-1] / temp)
            else:
                stack.append(int(n))
        return stack[0]