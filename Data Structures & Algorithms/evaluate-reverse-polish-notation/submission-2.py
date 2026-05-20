class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = ["+", "-", "*", "/"]

        for token in tokens:
            if token in operator:
                second_val = int(stack.pop())
                first_val = int(stack.pop())
                if token == "+":
                    result = first_val + second_val
                elif token == "-":
                    result = first_val - second_val
                elif token == "*":
                    result = first_val * second_val
                elif token == "/":
                    result = first_val / second_val
                stack.append(result)

            else:
                stack.append(token)

        return int(stack[-1])
            