class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check = {}
        for num in nums:
            check[num] = 1 + check.get(num,0)

        #create frequency bucket, each bucket is a list of number 
        freqMap = [[] for i in range(len(nums) + 1)]
        for num, cnt in check.items():
            #add number to list of number with same frequency
            freqMap[cnt].append(num)

        res = []
        for i in range(len(freqMap) - 1, 0, -1):
            for num in freqMap[i]:
                res.append(num)
                if len(res) == k:
                    return res

