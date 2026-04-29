class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        #  return index if target is found and if not, return where it could be inserted
        #  we can insert it where mid = 1 or, l== r

 
        l, r = 0, len(nums) - 1
        i = 0
        while l <= r:
            m = l + (r-l)//2
            if target < nums[m]:
                r = m -1
            elif target > nums[m]:
                l = m + 1
            elif target == nums[m]:
                return m
            
        return l 