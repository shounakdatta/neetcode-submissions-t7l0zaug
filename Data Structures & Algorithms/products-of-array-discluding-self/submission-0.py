class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        for n in nums:
            if n == 0:
                zero_count += 1
                continue
            prod *= n

        if zero_count > 1:
            return [0]*len(nums)
        
        res = []
        for n in nums:
            if n == 0:
                res.append(prod)
                continue
            if zero_count == 0:
                res.append(prod//n)
            else:
                res.append(0)
        return res

        