def medalSummary(medals: list, kind=None) -> dict:
    summary = {}
    for medal in medals:
        country = medal[0]
        if kind in (None, medal[4]):
            if country not in summary:
                summary[country] = 0
            summary[country] += 1
    return summary


def top(summary: dict, n=10) -> list:
    return sorted(summary.items(), key=lambda l: l[1], reverse=True)[:n]


with open('short.txt', 'r', encoding='utf-8') as file1, open('beijing_medals.txt', 'r', encoding='utf-8') as file2:
    from ast import literal_eval
    fencing1 = literal_eval(file1.read())
    fencing2 = literal_eval(file2.read())

print(top(medalSummary(fencing1), n=3))
print(top(medalSummary(fencing2), n=10))
