def add_fruit(basket: dict, fruit: str, amount=0):
    if fruit not in basket:
        basket[fruit] = 0
    basket[fruit] += amount
