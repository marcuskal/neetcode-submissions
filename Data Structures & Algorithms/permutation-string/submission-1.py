class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # need to create a fixed sliding window of size len(s1)
        # initial window starts from 0 - len(s1) -1
        # use fixed sliding window
        # with fixed window we build initial window

        # edge case

        if len(s1) > len(s2) or len(s1) < 1:
            return False

        fr = Counter(s1)
        wf = {}

        # build initial window
        for i in range(len(s1)):
            wf[s2[i]] = wf.get(s2[i], 0) + 1

        # compare initial window
        if wf == fr:
            return True

        # slide through the remaining
        for r in range(len(s1), len(s2)):
            wf[s2[r]] = wf.get(s2[r], 0) + 1
            left_char = s2[r - len(s1)]
            wf[left_char] -= 1
            if wf[left_char] == 0:
                del wf[left_char]

            if wf == fr:
                return True

        return False
                
