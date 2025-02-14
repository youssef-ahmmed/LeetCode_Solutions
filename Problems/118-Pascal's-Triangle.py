class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]

        for i in range(1, numRows):
            pascal.append(
                [1] + [a + b for a, b in pairwise(pascal[-1])] + [1]
            )

        return pascal
