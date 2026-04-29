class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        newArr = nums + [None]*n
        r = n
        l = 0
        while l < r:
            newArr[r + l] = nums[l]
            l += 1

        return newArr