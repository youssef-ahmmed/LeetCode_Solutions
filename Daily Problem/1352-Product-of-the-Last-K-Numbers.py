class ProductOfNumbers:
    def __init__(self):
        self.pre_mul = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.pre_mul = [1]
        else:
            self.pre_mul.append(num * self.pre_mul[-1])

    def getProduct(self, k: int) -> int:
        n = len(self.pre_mul)
        return 0 if k >= n else self.pre_mul[-1] // self.pre_mul[n - k - 1]
