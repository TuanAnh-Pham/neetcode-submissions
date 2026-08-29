class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        barStack = []
        currMax = 0

        for i,h in enumerate(heights):
            start = i
            while barStack and barStack[-1][1] > h:
                index, height = barStack.pop()
                currMax = max(currMax, height * (i - index))
                start = index

            barStack.append((start,h))

        for i, h in barStack:
            currMax = max(currMax, h * (len(heights) - i))

        return currMax