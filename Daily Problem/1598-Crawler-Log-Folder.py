class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0

        for log in logs:
            if log.startswith('./'):
                continue
            elif log.startswith('../') and cnt:
                cnt -= 1
            elif log[0].isalnum():
                cnt += 1

        return cnt
        