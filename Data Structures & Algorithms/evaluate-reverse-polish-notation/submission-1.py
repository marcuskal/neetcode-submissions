class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # use a stack to track state of operation results
        rec = []
        for i in range(len(tokens)):
            if tokens[i] == "+":
                b, a = rec.pop(), rec.pop()
                rec.append(a + b)
            elif tokens[i] == "-":
                b, a = rec.pop(), rec.pop()
                rec.append(a - b)
            elif tokens[i] == "*":
                b, a = rec.pop(), rec.pop()
                rec.append(a * b)
            elif tokens[i] == "/":
                b, a = rec.pop(), rec.pop()
                rec.append(int(a / b))
            else:
                rec.append(int(tokens[i]))

        return rec[0]