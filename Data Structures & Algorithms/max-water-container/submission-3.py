class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = base * heigh
        # base is the distance between the hieghts
        # height is the heights[i]
        # height is the min of the two heights
        # we're looking for the max area, max bh.
        # we can use a hash table to store the height
        # And always store the max area until we reach the end

        # 1. we need to loop through the array and update the hashtable

        maxArea = 0

        l, r = 0, len(heights) - 1

        while l < r:

            # base = distance between l and r, or r-l
            # heigh, min of l and r
            h = min(heights[r], heights[l])
            b = r-l
            area = h * b
            maxArea= max(maxArea, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea
