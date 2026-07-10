class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        result = []
        m = max(candies)
        for i in range(0,n):
            if candies[i]+extraCandies >= m:
                result.append(True)
            else:
                result.append(False)
        return result
    