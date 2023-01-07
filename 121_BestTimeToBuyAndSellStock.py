# 121. Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan&id=data-structure-i


from typing import List

def maxProfit(self, prices: List[int]) -> int:
        l, r =0, 1
        max_profit = 0
        while(r < len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else :
                l = r
            r +=1
        return max_profit