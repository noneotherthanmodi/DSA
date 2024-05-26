from typing import List 


def maxProfit(prices: List[int]) -> int:
    sum = 0
    maxi = 0
    a = prices[0]
    n = len(prices)
    for i in range(n):
        if(prices[i+1]>prices[i]):
            b = prices[i+1] - prices[i]
    pass