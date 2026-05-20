class Solution:
    def isValid(self, s: str) -> bool:
        closeMap = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }

        stack = []

        for c in s:
            if c in closeMap:   
                if stack and closeMap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        
        return not stack