class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # edge case
        if target < nums[0] or target > nums[-1]:
            return - 1
        l, r = 0, len(nums) -1
        # find the middle ground and go to the right or left depending on target

        while l <= r:
            #  this way of doing it, fixes an overflow error
            m = l + (r-l)//2

            if target < nums[m]:
                r = m -1
            elif target > nums[m]:
                l = m + 1
            else:
                return m
        
        return -1