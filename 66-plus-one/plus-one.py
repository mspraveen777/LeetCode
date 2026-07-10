class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        res = 0
        ans = []
        for num in digits:
            res= res*10 + num
        res += 1
        while res > 0:
            ld = res % 10
            ans.append(ld)
            res = res//10
        ans.reverse()
        return ans


        # for i in range(n-1,-1,-1):
        #     if digits[i] < 9:
        #         digits[i] += 1
        #         return digits
            
        #     digits[i]= 0
            
        #     return [1] + digits

        