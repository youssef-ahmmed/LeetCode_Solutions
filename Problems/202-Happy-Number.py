class Solution:
    def isHappy(self, n: int) -> bool:
        # Example:
        # 2 => 2 ^ 2 = 4
        # 4 => 4 ^ 2 = 16
        # 16 = 1 ^ 2 + 6 ^ 2 = 37
        # 37 = 3 ^ 2 + 7 ^ 2 = 58
        # 58 = 5 ^ 2 + 8 ^ 2 = 89
        # 89 = 8 ^ 2 + 9 ^ 2 = 145
        # 145 = 1 ^ 2 + 4 ^ 2 + 5 ^ 2 = 42
        # 42 = 4 ^ 2 + 2 ^ 2 = 20
        # 20 = 2 ^ 2 + 0 ^ 2 = 4
        # We reach 4 before

        def digits_square(m):
            sq = 0
            while m:
                a = m % 10
                sq += a ** 2
                m //= 10

            return sq

        nums = set()
        sq = n

        while True:
            sq = digits_square(sq)

            if sq in nums:
                return False
            if sq == 1:
                return True

            nums.add(sq)
