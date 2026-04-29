class Solution:
    def isPalindrome(self, s: str) -> bool:
        # palindromes are monotonic so we use two pointers

        # setup the two pointers, left and right

        left, right = 0, len(s) -1

        # move pointers one from left, one from right
        while left < right:
        
        # skip then compare pattern needs to be implemented here
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1
        return True
        