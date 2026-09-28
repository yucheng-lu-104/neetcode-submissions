class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        res = True

        for char in s:
            if char in ('(', '{', '['):
                stack.append(char)
            if char in (')', '}', ']'):
                if len(stack) == 0:
                    res = False
                elif (
                    (char == ')' and stack.pop() != '(') or
                    (char == '}' and stack.pop() != '{') or
                    (char == ']' and stack.pop() != '[')
                ):
                    res = False

        if len(stack) != 0:
            res = False
        
        return res