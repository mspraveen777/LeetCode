class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        curru = 0
        finalunit = 0
        for i in range(0,len(boxTypes)):
            if curru + boxTypes[i][0] <= truckSize:
                curru += boxTypes[i][0]
                finalunit += boxTypes[i][1]*boxTypes[i][0] 
            else:
                remaining = truckSize - curru
                finalunit += boxTypes[i][1]*remaining
                break

        return finalunit
        