from typing import List


def maxProfitBruteForce(prices: List[int]) -> int:
    profit = 0
    for i, price in enumerate(prices[:-1]):
        diff = max(prices[i + 1:]) - price
        if diff > profit:
            profit = diff

    return profit


def maxProfitSolOne(prices: List[int]) -> int:
    """This is the one of the solution of the famous LeetCode problem of best time to buy and sell
    stock. The given array are the prices of a stock on i^th day. We need to return the maximum
    profit one can achieve with this transaction.

    Here needs a little explanation.We want to maximize the profit. In order to do so, our initial min
    price would be maximum i.e., infinity and profit is zero. As we navigate through the prices one by one,
    the min price would be the minimum of the minPrice and the current price, whereas profit would be the
    max of the previous profit and difference between current price and min price.

    Args:
        prices(List[int]): An array of prices

    Returns:
        int: The max profit that can be achieved with these transactions.
    """
    minPrice = float('inf')
    profit = 0

    for price in prices:
        minPrice = min(price, minPrice)
        profit = max(profit, price - minPrice)

    return profit


def maxProfit(prices: List[int]) -> int:
    """This is the optimized solution of this problem. We are comparing the buying price and the current
    price and accordingly updating the profit.

    Args:
        prices(List[int]): An array of prices

    Returns:
        int: The max profit that can be achieved with these transactions.
    """
    profit = 0
    buyPrice = prices[0]
    for price in prices:
        if price < buyPrice:
            buyPrice = price
        else:
            profit = max(profit, price - buyPrice)

    return profit


if __name__ == "__main__":
    print(maxProfitBruteForce([7, 1, 5, 3, 6, 4]))
    print(maxProfitBruteForce([7, 6, 4, 3, 1]))
    print(maxProfitBruteForce([1, 2]))
    print(maxProfitBruteForce([2, 4, 1]))
    print()
    print(maxProfitSolOne([7, 1, 5, 3, 6, 4]))
    print(maxProfitSolOne([7, 6, 4, 3, 1]))
    print(maxProfitSolOne([1, 2]))
    print(maxProfitSolOne([2, 4, 1]))
    print()
    print(maxProfit([7, 1, 5, 3, 6, 4]))
    print(maxProfit([7, 6, 4, 3, 1]))
    print(maxProfit([1, 2]))
    print(maxProfit([2, 4, 1]))

