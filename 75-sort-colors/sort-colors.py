class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = 0
        while left < n:
            for i in range(left + 1, n):
                if nums[i] < nums[left]:
                    nums[left ], nums[i] = nums[i], nums[left]
            left += 1
        return nums
