class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # n = len(nums)
        c1 = 0
        for i in nums:
            count = 0

            while i > 0:
                i = i// 10
                count+=1

            if count % 2 == 0:
              c1 += 1
            
        return c1

            