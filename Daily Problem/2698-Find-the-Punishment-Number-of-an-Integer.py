class Solution:
    def punishmentNumber(self, n: int) -> int:
        def can_partition(curr_idx: int, curr_sum: int, target: int, num_str: str):
            if curr_idx == len(num_str):
                return curr_sum == target

            for i in range(curr_idx, len(num_str)):
                if can_partition(i + 1, curr_sum + int(num_str[curr_idx : i + 1]), target, num_str):
                    return True
            
            return False

        res = 0
        for i in range(1, n + 1):
            if can_partition(0, 0, i, str(i * i)):
                res += i * i

        return res
