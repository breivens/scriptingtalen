def addProduct(shoppingcart: dict, product: str, amount=0):
    if amount < 0:
        return 0
    if product not in shoppingcart:
        shoppingcart[product] = 0
    shoppingcart[product] += amount
    return shoppingcart[product]


def removeProduct(shoppingcart: dict, product: str, amount=1):
    if product not in shoppingcart:
        return 0
    if amount < shoppingcart[product]:
        shoppingcart[product] -= amount
        return shoppingcart[product]
    del shoppingcart[product]
    return 0
