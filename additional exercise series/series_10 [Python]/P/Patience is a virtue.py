class PatienceSorter:
    def __init__(self):
        self._stacks = list()

    def stacks(self):
        return self._stacks

    def stack_count(self):
        return len(self._stacks)

    def item_count(self):
        return sum(map(len, self._stacks))

    def add_item(self, item: int):
        for i, stack in enumerate(self._stacks):
            if item <= stack[0]:
                self._stacks[i].insert(0, item)
                return self
        self._stacks.append([item])
        return self

    def add_items(self, sequence: list or tuple):
        for item in sequence:
            self.add_item(item)
        return self

    def remove_item(self):
        assert self._stacks, "no more items"
        min_stack = min(self._stacks, key=lambda s: s[0])
        for i, stack in enumerate(self._stacks):
            if stack == min_stack:
                item = self._stacks[i].pop(0)
                self._stacks = list(filter(None, self._stacks))
                return item
        return None

    def remove_items(self):
        items = list()
        while self._stacks:
            items.append(self.remove_item())
        return tuple(items)
