class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 0 and n not in seen:
            seen.add(n)
            num = n
            res = 0
            while num > 0 :
                ld = num % 10
                res += ld**2
                num //= 10
            n = res
        
        return n == 1


        