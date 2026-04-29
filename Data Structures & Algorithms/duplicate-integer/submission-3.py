class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num in nums:
            if num in freq and freq[num] >= 2:
                return True
        return False