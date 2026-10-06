class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # left = 0
        # while left < n:
        #     for i in range(left + 1, n):
        #         if nums[i] < nums[left]:
        #             nums[left ], nums[i] = nums[i], nums[left]
        #     left += 1
        # return nums

        n = len(nums)
        mid = 0
        low = 0
        high = n-1
        while mid <= high:
            if nums[mid] == 0:
                nums[low],nums[mid] = nums[mid],nums[low]
                mid +=1
                low+=1
            elif nums[mid] == 1:
                mid +=1
            else:
                nums[mid],nums[high] = nums[high],nums[mid]
                high -= 1
        return nums
            
