class Solution:
    def isValid(self, s: str) -> bool:
        closeMap = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }

        stack = []

        for bucket in s:
            if bucket in closeMap:   
                if stack and closeMap[bucket] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bucket)

        
        return not stack