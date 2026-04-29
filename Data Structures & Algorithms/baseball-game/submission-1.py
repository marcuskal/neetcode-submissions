class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec = []

        for i in range(len(operations)):
            if operations[i] == "C":
                rec.pop()

            elif operations[i] == "+":
                summ = rec[-1] + rec[-2]
                rec.append(summ)
            
            elif operations[i] == "D":
                score = 2 * rec[-1]
                rec.append(score)
            else:
                rec.append(int(operations[i]))
        return sum(rec)