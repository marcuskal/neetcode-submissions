class Solution:
    def mySqrt(self, x: int) -> int:
        # how to find the square root
        # what is a square root of x?
        # if n*n = x then n is the square root
        # how to solve with binary search
        # start from 0 to n
        # try to square n and compare with x
        # if n squared < x > n+1 squared, we return n


        l, r = 0, x

        while l <= r:
            m = l + (r-l)//2
            res = m * m

            if res == x:
                return m

            elif res < x:
                l = m + 1
            elif res > x:
                r = m - 1
        return r