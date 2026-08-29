class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l =  len(temperatures)
        dayWarm = [0] * l

        stack = []

        for t in range(l):
            
            while stack and temperatures[stack[-1]] < temperatures[t]:
                dayWarm[stack[-1]] = t - stack[-1]
                stack.pop()

            stack.append(t)
        return dayWarm