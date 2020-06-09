from re import search, sub


def is_valid_plan(plan):
    bitcoin = 0
    for action in plan:
        bitcoin += {"S": -1, "B": 1}.get(action, 0)
        if bitcoin not in (0, 1):  # can only be 0 or 1
            return False
    if bitcoin != 0:  # no leftovers allowed
        return False
    return True


def is_valid_plan_alt(plan):  # prob slower
    plan = plan.replace("-", "")
    return plan[0] == "B" != plan[-1] and not bool(search(r"(\w)\1+", plan))


def profit(exchange_rate, plan):
    assert (isinstance(plan, str) and len(exchange_rate) == len(plan) and sub("[BS-]", "", plan) == "" and
            is_valid_plan(plan)), "ongeldige acties"
    wallet = 0
    for a, action in enumerate(plan):
        if action == "B":
            wallet -= exchange_rate[a]
        elif action == "S":
            wallet += exchange_rate[a]
    return wallet


def optimal_actions(exchange_rate):
    plan, bitcoin = "", False
    for i in range(len(exchange_rate) - 1):
        if not bitcoin and exchange_rate[i] < exchange_rate[i + 1]:
            bitcoin = True
            plan += "B"
        elif bitcoin and exchange_rate[i] > exchange_rate[i + 1]:
            bitcoin = False
            plan += "S"
        else:
            plan += "-"
    plan += "S" if bitcoin else "-"
    return plan


def maximal_profit(exchange_rate):
    return profit(exchange_rate, optimal_actions(exchange_rate))


# alternate solution
"""
def profit(exchange_rate, plan):
    assert (isinstance(plan, str) and len(exchange_rate) == len(plan)), "ongeldige acties"
    assert (("".join([char for char in plan if char not in "BS-"])) == ""), "ongeldige acties"
    assert (is_valid_plan(plan)), "ongeldige acties"
    wallet = 0
    for i, action in enumerate(plan):
        if action == "B":
            wallet -= exchange_rate[i]
        elif action == "S":
            wallet += exchange_rate[i]
    return wallet


def iterate(exchange_rate):
    plan, wallet, bitcoin = "", 0, 0
    
    try:
        for i in range(len(exchange_rate)):
            if bitcoin == 0 and exchange_rate[i] < exchange_rate[i+1]:
                bitcoin = 1
                wallet -= exchange_rate[i]
                plan += "B"
            elif bitcoin == 1 and exchange_rate[i] > exchange_rate[i+1]:
                bitcoin = 0
                wallet += exchange_rate[i]
                plan += "S"
            else:
                plan += "-"
        return wallet, plan
    except IndexError:
        if bitcoin == 1:
            bitcoin -= 1
            wallet += exchange_rate[-1]
            plan += "S"
        else:
            plan += "-"
        return wallet, plan


def maximal_profit(exchange_rate):
    return iterate(exchange_rate)[0]


def optimal_actions(exchange_rate):
    return iterate(exchange_rate)[1]
"""
