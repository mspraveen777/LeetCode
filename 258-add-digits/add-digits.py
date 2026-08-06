class Solution:
    def addDigits(self, num: int) -> int:
        n = num 
        while len(str(n)) != 1:
            res = 0

            while n > 0:
                ld = n % 10
                res +=ld
                n = n //10
            n = res
        return n
        