class Solution:
    def calPoints(self, operations: List[str]) -> int:
        n = len(operations)
        res = []

        for i in range(n):
            if operations[i] == "+":
                res.append(res[-1] + res[-2])
            elif operations[i] == "D":
                res.append(res[-1] * 2)
            elif operations[i] == "C":
                if len(res) > 0:
                    res.pop()
            else:
                res.append(int(operations[i]))
        
        return sum(res)
