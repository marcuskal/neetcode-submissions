class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if len(s) != len(t):
        #     return False

        # freq = {}

        # for ch in s:
        #     freq[ch] = freq.get(ch, 0) + 1
        # for ch in t:
        #     if ch not in freq or freq[ch] == 0:
        #         return False
        #     freq[ch] -= 1
        # return True
        
        # edge case
        if len(s) != len(t):
            return False
        
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        for char in t:
            if char not in freq or freq[char] == 0:
                return False
            freq[char] -= 1
        return True