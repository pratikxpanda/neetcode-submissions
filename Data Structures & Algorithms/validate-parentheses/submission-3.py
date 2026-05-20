class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        isValid = True

        for bracket in s:
            if bracket == "(" or bracket == "{" or bracket == "[":
                stack.append(bracket)
            elif bracket == ")":
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    isValid = False
                    break
            elif len(stack) > 0 and bracket == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    isValid = False
                    break
            elif len(stack) > 0 and bracket == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    isValid = False
                    break
            else:
                isValid = False
                break
        
        if len(stack) != 0:
            isValid = False
        
        return isValid