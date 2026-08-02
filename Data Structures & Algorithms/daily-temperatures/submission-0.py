class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        l = [0] * len(temperatures)

        for i in range(len(temperatures)):
            nums = temperatures[i]

            while stack and temperatures[stack[-1]] < nums:
                previous_day = stack.pop()
                l[previous_day] = i - previous_day

            stack.append(i)

        return l