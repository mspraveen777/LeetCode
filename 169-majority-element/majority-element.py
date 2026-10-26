class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0
        element = 0
        for i in range(n):
            if count == 0:
                element = nums[i]
                count =1
            elif nums[i] == element:
                count +=1
            else:
                count-=1

        return element
        