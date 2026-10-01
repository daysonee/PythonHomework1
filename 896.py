class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:

        plus = minus = True
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                plus = False
            if nums[i - 1] < nums[i]:
                minus = False

        if plus == True or minus == True:
            return True
        return False
