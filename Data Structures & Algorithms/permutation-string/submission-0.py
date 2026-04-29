class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # need to create a fixed sliding window of size len(s1)
        # initial window starts from 0 - len(s1) -1
        # use a set to check the permutation

        # set the char_set
        # char_set = set(s1)
        l = 0
        window = len(s1) - 1


        # create window
        for r in range(window, len(s2)):
            if Counter(s2[l:r+1]) == Counter(s1):
                return True
            else:
                l +=1
                # r +=1
        
        return False
                
