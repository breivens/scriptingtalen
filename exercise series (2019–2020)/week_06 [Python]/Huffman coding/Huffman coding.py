from csv import reader

class Node:
    def __init__(self, symbol=None, left=None, right=None):
        self.left = left
        self.right = right
        self.symbol = symbol

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_symbol(self):
        return self.symbol

    def add_child(self, bitstring, symbol):
        bit, bitstring = bitstring[0], bitstring[1:]
        if bit == "0":
            node = self.left if self.left is not None else Node()
            self.left = node
        else:
            node = self.right or Node()
            self.right = node

        if len(bitstring) == 0:
            node.symbol = symbol
        else:
            node.add_child(bitstring, symbol)


class Huffman:
    def __init__(self, path):
        self.root = Node()
        with open(path, "r") as file:
            self.values = dict(reader(file, delimiter='\t'))
        for symbol, bitstring in self.values.items():
            self.root.add_child(bitstring, symbol)

    def codeer(self, s):
        output = ""
        for c in s:
            try:
                output += self.values[c]
            except KeyError:
                raise ValueError(f'onbekend symbool "{c}"')
        return output

    def decodeer(self, bitstring):
        output = ""
        node = self.root

        while len(bitstring) > 0:
            bit, bitstring = bitstring[0], bitstring[1:]
            if bit == "0":
                new_node = node.left
            else:
                new_node = node.right
            if new_node is None:
                raise ValueError("ongeldige bitstring")

            if (symbol := new_node.symbol) is not None:
                output += symbol
                node = self.root
            else:
                node = new_node

        if node is not self.root:
            raise ValueError("ongeldige bitstring")

        return output

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node):
        if node is not None:
            self._print_tree(node.left)
            print(f'<"{node.symbol}">' if isinstance(node.symbol, str) else f"<{node.symbol}>", end=' ')
            self._print_tree(node.right)


h = Huffman('codes.txt')
h.print_tree()
print(h.root.get_left().get_left().get_left().get_symbol())
print(h.root.left.left.left.symbol)