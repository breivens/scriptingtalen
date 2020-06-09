def combine(colors: list or tuple, fruits: list or tuple, amount=float('inf')):
    from random import sample
    n = min(len(colors), len(fruits), amount)
    return [f'a {c} {f}' for c, f in zip(sample(colors, k=n), sample(fruits, k=n))]


colors = ['purple', 'yellow', 'green']
fruits = ('grape', 'banana', 'apple')
print(combine(colors, fruits))
# ['a purple grape', 'a green banana', 'a yellow apple']
print(combine(colors, fruits))
# ['a purple grape', 'a green apple', 'a yellow banana']
print(combine(colors, fruits))
# ['a purple apple', 'a yellow grape', 'a green banana']
print(combine(colors, fruits, amount=1))
# ['a purple grape']
print(combine(colors, fruits, amount=2))
# ['a yellow apple', 'a green banana']
print(combine(colors, fruits, amount=4))
# ['a yellow banana', 'a green grape', 'a purple apple']
