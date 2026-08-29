class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr_max = 1
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        # build hash set 
        for num in nums:
            curr_length = 1
            curr = num 
            while (curr + 1) in nums:
               curr_length += 1
               curr = curr + 1  
               if curr_length > curr_max:
                    curr_max = curr_length

        return curr_max

        # for item in possible start 
            #init max leng
            # while num - 1 still in hash, leng +1 
                #update max if leng > max
        #return max
             

        