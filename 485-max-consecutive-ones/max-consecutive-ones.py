class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        cnt = 0
        max_cnt = 0
        for i in range(0,len(nums)):
            if nums[i] == 1:
                cnt +=1
            else:
                max_cnt = max(max_cnt,cnt)
                cnt = 0
        return max(max_cnt,cnt)
        