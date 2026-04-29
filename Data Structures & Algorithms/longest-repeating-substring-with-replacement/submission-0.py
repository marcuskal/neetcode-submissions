class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # find out the longest non reapting
        # can replace up to k times of the longest char
        # maintain a state of the window
        # replace k times, meaning, we can move forward twice after
        # a char stop reapeating
        # while j < k:
        # if s[i] ! = s[i + 1]
        # dynamic window


        n = len(s)
        char_set = {}
        max_length = 0
        left = 0


        # EXPAND right, SHRINK left, UPDATE result
        for r in range(n):
            # add s[r] to char_set
            char_set[s[r]] = char_set.get(s[r], 0) + 1
            #update frequency
            max_freq = max(char_set.values())
            # shrink while invalide
            while(r - left + 1) - max_freq > k:
                char_set[s[left]] -= 1
                if char_set[s[left]] == 0:
                    del char_set[s[left]]
                left +=1
            max_length = max(max_length, r - left + 1)

        return max_length

