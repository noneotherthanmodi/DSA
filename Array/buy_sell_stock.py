from typing import List 


def maxProfit(prices: List[int]) -> int:
    mini = prices[0]
    profit = 0  
    n = len(prices)
    for i in range(1,n):
        cost = prices[i] - mini
        profit = max(cost,profit)
        mini = min(mini,prices[i])
    
    print(profit)

maxProfit([7,6,4,3,1])
    