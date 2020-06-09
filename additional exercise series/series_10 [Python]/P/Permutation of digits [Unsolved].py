class DigitPermutation:
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        number = str(self.number)[::-1]  # reverse
        # find index to split number
        prev_digit = number[0]
        index = None
        for i, digit in enumerate(number):
            if digit < prev_digit:  # increasing
                index = i  # index found
                break
            prev_digit = digit
        # abort if index not found
        if index is None:
            raise StopIteration
        # split number
        left, right = list(number[index:][::-1]), list(number[:index])
        # find index from right side to swap
        index = ''.join(right).rindex(min([digit for digit in right if digit > left[-1]]))
        # swap numbers
        left[-1], right[index] = right[index], left[-1]
        # update class attribute
        self.number = int(''.join(left + right))  # concatenate and convert to int
        return self.number


iter = DigitPermutation(135798642)
print(next(iter))
print(next(iter))

iter = DigitPermutation(123)
for next_element in iter:
    print(next_element)
