class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for nums in tokens:
            if nums not in operators:
                stack.append(int(nums))

            else:
                first = stack.pop()
                second = stack.pop()

                if nums == "+":
                    stack.append(second + first)

                elif nums == "-":
                    stack.append(second - first)

                elif nums == "*":
                    stack.append(second * first)

                elif nums == "/":
                    stack.append(int(second / first))

        return stack[-1]