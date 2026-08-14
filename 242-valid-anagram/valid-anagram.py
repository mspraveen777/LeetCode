class Solution:
    def isAnagram(self, s: str, t) -> bool:
        if len(s)!= len(t):
            return False
        hash_dict1 = {}
        hash_dict2 = {}
    
        for ch in s:
            if ch in hash_dict1:
                hash_dict1[ch] +=1
            else:
                hash_dict1[ch] = 1
        for ch in t:
                if ch in hash_dict2:
                    hash_dict2[ch] +=1
                else:
                    hash_dict2[ch] = 1


        if hash_dict1 == hash_dict2:
            return True
        else:
            return False
    

        