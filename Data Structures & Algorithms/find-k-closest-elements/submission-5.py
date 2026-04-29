class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # two pointers will be used
        # has monotonic behavior

        l, r = 0, len(arr) - 1

        # shrink the window unitl k size is reached
        while r - l + 1 > k:
            # remove the farthest side, if left or right
            if x - arr[l] > arr[r] - x:
                l += 1
            else:
                r -= 1
        # return the k window subarray
        return arr[l: r+1]