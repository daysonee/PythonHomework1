class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        s = f = nums[0]
        s = nums[s]
        f = nums[nums[f]]
        while s != f:
            s = nums[s]
            f = nums[nums[f]]

        f = nums[0]
        while s != f:
            s = nums[s]
            f = nums[f]
        return s
