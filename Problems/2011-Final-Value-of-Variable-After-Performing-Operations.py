class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        num = 0

        for op in operations:
            if op == '--X' or op == 'X--':
                num -= 1
            else:
                num += 1
        
        return num
