class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxi = float("-inf")
        tot = 0
        n = len(nums)
        for i in range(0,n):
            tot += nums[i]
            maxi = max(maxi,tot)
            if tot < 0:
                tot = 0
        return maxi

        