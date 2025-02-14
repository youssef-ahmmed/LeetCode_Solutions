class ProductOfNumbers:

    def __init__(self):
        self.data = []
        self.pre_mul = []
        self.zero_idx = 0

    def add(self, num: int) -> None:
        self.data.append(num)
        self.zero_idx = len(self.data) - 1

        self.update_prefix_mul(num)

    def getProduct(self, k: int) -> int:
        n = len(self.pre_mul)
        if k > n:
            return 0
        if k == n:
            return self.pre_mul[-1]
        return self.pre_mul[-1] // self.pre_mul[n - k - 1]
    
    def update_prefix_mul(self, num: int) -> None:
        if num == 0:
            self.pre_mul.clear()
            return

        if len(self.pre_mul) == 0:
            self.pre_mul.append(num)
        else:
            self.pre_mul.append(num * self.pre_mul[-1])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)