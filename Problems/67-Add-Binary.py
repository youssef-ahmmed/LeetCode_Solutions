class Solution:
    def addBinary(self, a: str, b: str) -> str:
        mx_sz = max(len(a), len(b))

        b1 = a.zfill(mx_sz)
        b2 = b.zfill(mx_sz)

        res = ''
        carry = 0
        for i in range(mx_sz - 1, -1, -1):
            s = carry + int(b1[i]) + int(b2[i])
            if s == 2:
                res += '0'
                carry = 1
            elif s == 3:
                res += '1'
                carry = 1
            else:
                res += str(s)
                carry = 0

        if carry:
            res += '1'

        return res[::-1]