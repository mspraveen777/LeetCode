class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left , right+1):
            n = i
            valid = True
            while n > 0:
                ld = n % 10
                if ld == 0 or  i % ld !=0:
                    valid = False
                    break
                n = n//10
            if valid == True:
                res.append(i)
        return res
                

        return res       