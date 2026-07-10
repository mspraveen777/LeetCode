class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
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


        