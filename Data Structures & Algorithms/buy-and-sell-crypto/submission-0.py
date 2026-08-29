class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMax = 0
        buy = prices[0]

        for p in range(1,len(prices)):
            if prices[p] < buy:
                buy = prices[p]
            else:
                currMax = max(currMax,prices[p]-buy)
        
        return currMax

