class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        decode = [0] * n

        l = 0
        w_sum = 0
        for r in range(n + abs(k)):
            w_sum += code[r % n]

            if r - l + 1 > abs(k):
                w_sum -= code[l % n]
                l = (l + 1) % n

            if r - l + 1 == abs(k):
                if k > 0:
                    decode[(l - 1) % n] = w_sum
                elif k < 0:
                    decode[(r + 1) % n] = w_sum

        return decode
