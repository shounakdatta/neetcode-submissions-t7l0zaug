class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums)//2
        if nums[mid] == target:
            return mid
        if len(nums) == 1:
            return -1
        val = -1
        if target < nums[mid]:
            # print('search', nums[:mid], target)
            val = self.search(nums[:mid], target)  
        else:
            # print('search', nums[mid:], target)
            val = self.search(nums[mid:], target)
            if val > -1:
                val += mid
        return val
