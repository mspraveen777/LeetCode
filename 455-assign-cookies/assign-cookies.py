class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        left = 0
        right = 0
        n = len(g)
        m = len(s)
        count = 0
        while left < n and right < m:
            if s[right] >= g[left]:
                count += 1 
                left+=1
            right+=1
        return count

        