class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0

        for op in operations:
            if op == "+":
                sum = stack[-1] + stack[-2]
                res += sum
                stack.append(sum)
            elif op == "D":
                double = 2 * stack[-1]
                res += double
                stack.append(double)
            elif op == "C":
                res -= stack.pop()
            else:
                val = int(op)
                res += val
                stack.append(val)
        
        return res