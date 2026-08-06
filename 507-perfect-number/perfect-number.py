from math import sqrt
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        res = 0
        for i in range(1,int(sqrt(num)+1)):
            if num % i == 0:
                res += i
                if num//i != i:
                    res += num//i
        res -= num
        if res == num:
            return True
        else: 
            return False
        