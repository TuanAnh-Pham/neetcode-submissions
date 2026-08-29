class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = 0

        result = []
        for i in nums:
            if i != 0:
                total_product = total_product * i
            else:
                zero_count += 1

        if zero_count > 1:
            return [0] * len(nums) 


        for i,c in enumerate(nums):
            if zero_count == 1:
                if c != 0:
                    result.append(0)
                else:
                    result.append(total_product)
            else:
                result.append(total_product//c)
        return result

