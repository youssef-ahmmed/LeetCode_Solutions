class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = list(map(int, version1.split('.')))
        ver2 = list(map(int, version2.split('.')))

        for a1, a2 in zip_longest(ver1, ver2, fillvalue=0):
            if a1 == a2:
                continue
            return -1 if a2 > a1 else 1

        return 0
        