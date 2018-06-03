'''
Write a program that takes an array denoting the daily stock price,
and returns the maximum profit that could be made by buying,and then selling one
share of that stock. There if no need to buy if no profit is possible
'''

# O(N) time, O(1) space
def maximum_single_sell(prices):
    min_price, max_profit = float('inf'), 0.0
    for price in prices:
        min_price = min(price, min_price)
        max_profit = max(price - min_price, max_profit)
    return max_profit


A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print('Maximum profit {}'.format(maximum_single_sell(A)))
