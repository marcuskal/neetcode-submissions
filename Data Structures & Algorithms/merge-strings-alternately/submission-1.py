class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        # create a new array to store the chars
        res = []
        w1, w2 = 0, 0
        for i in range(len(word1) - 1):
            res.append(word1[i])
            w1 += 1
            if w2 < len(word2):
                res.append(word2[i])
                w2 +=1
        
        res.append(word1[w1:])
        res.append(word2[w2:])


        return "".join(res)