class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()

        for num in arr:
            if num * 2 in seen or (num & 1 == 0 and num // 2 in seen):
                return True

            seen.add(num)

        return False
