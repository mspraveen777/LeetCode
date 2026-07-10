class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range (0,n):
            count = 0
            for j in range(0,n):
                if nums[i] > nums[j]:
                    count += 1
            
            res.append(count)
                
        return res

        