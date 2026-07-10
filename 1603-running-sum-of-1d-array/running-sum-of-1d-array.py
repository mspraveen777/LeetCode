class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = 0
        lst = []
        n = len(nums)
        for i in range(0,n):
            res += nums[i]
            lst.append(res)
        return lst

        