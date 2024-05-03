class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = list(map(lambda n: int(n), version1.split('.')))
        ver2 = list(map(lambda n: int(n), version2.split('.')))

        sz1, sz2 = len(ver1), len(ver2)

        if sz1 < sz2:
            ver1.extend([0] * (sz2 - sz1))
        elif sz1 > sz2:
            ver2.extend([0] * (sz1 - sz2))

        if ver1 > ver2:
            return 1
        elif ver2 > ver1:
            return -1
        
        return 0

        