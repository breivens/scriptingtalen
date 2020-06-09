def together(prices):
    prices = sorted(prices)
    cheapest = sum(prices[:len(prices) // 4])
    return sum(prices) - cheapest


def group(prices):
    prices = sorted(prices, reverse=True)
    return [tuple(prices[i:i + 4]) for i in range(0, len(prices), 4)]


def grouped(prices):
    discount = sum(min(groep) for groep in group(prices) if len(groep) == 4)
    return round(sum(prices) - discount, 2)


def profit(prices):
    return round(together(prices) - grouped(prices), 2)
