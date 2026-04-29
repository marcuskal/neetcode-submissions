class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # dynamic sliding window problem
        # find window where sum(window) > = target
        # keep track of the min window length

        wlength = float('inf')
        l = 0
        summ = 0

        for r in range(len(nums)):
            summ += nums[r]
            while summ >= target:
                wlength = min(wlength, r-l + 1)
                summ -= nums[l]
                l += 1
        return 0 if wlength == float('inf') else wlength