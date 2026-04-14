class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)
        for l in range(len(nums)-1):
            m = l+1
            r = len(nums)-1
            if nums[l] > 0:
                break
            if l > 0 and nums[l] == nums[l-1]:
                continue
            while m < r:
                t = nums[l]+nums[m]+nums[r]
                if t == 0:
                    res.append([nums[l], nums[m], nums[r]])
                    m += 1
                    r -= 1
                    while nums[m] == nums[m-1] and m < r:
                        m += 1
                elif t < 0:
                    m += 1
                else:
                    r -= 1
        return res