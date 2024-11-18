class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        decode = [0] * n

        if k == 0:
            return decode

        for i in range(n):
            if k > 0:
                for j in range(1, k + 1):
                    decode[i] += code[(i + j) % n]
            else:
                for j in range(k, 0):
                    decode[i] += code[(i + j) % n]

        return decode
