class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [[1]]

        for i in range(1, rowIndex + 1):
            pascal.append(
                [1] + [a + b for a, b in pairwise(pascal[-1])] + [1]
            )

        return pascal[rowIndex]
