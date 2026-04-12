class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = {}
        for i, n in enumerate(numbers):
            nums[n] = i+1
        for n1 in numbers:
            n2 = target-n1
            if n2 != n1 and n2 in nums:
                i = nums[n1]
                j = nums[n2]
                return [i,j] if i<=j else [j,i]
        