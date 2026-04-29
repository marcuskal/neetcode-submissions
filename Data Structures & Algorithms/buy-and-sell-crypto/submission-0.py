class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # need to store max profit.
        # need to check the buy now and sell later
        # we can only move in one direction
        # if no profitanl transaction, we return 0
        # we use sliding window technique with the pointer 
        # moving forward, with variable speed


        maxProfit = 0
        left = 0

        for right in range(1, len(prices)):
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit,  profit)

            if prices[right] < prices[left]:
                left = right

        return maxProfit
