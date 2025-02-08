class NumberContainers:

    def __init__(self):
        self.number_positions = defaultdict(SortedSet)
        self.index_number = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index_number:
            self.number_positions[self.index_number[index]].discard(index)
            if len(self.number_positions[self.index_number[index]]) == 0:
                del self.number_positions[self.index_number[index]]

        self.index_number[index] = number
        self.number_positions[number].add(index)

    def find(self, number: int) -> int:
        if number in self.number_positions:
            return self.number_positions[number][0]
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)