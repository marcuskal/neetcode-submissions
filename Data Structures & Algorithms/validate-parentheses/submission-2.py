class Solution:
    def isValid(self, s: str) -> bool:
        # create an empty stack
        stack = []
        chars = {")":"(", "}":"{","]":"["}

        for c in s:
            if c in chars:
                if not stack or chars[c] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0