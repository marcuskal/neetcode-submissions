class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # I need state maintanance
        # I need to store the max
        # i will use a hashset and two pointers

        longest = 0
        sett = set()
        left = 0

        for right in range(len(s)):
            # handle inavlid window
            while s[right] in sett:
                sett.remove(s[left])
                left += 1

            # handle valid window
            width =  (right - left) + 1
            longest = max(longest, width)
            sett.add(s[right])
        return longest
        