class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait_time = 0
        current_time = 0

        for arrival_time, prep_time in customers:
            if current_time < arrival_time:
                current_time = arrival_time

            finish_time = current_time + prep_time
            wait_time += finish_time - arrival_time

            current_time = finish_time

        return wait_time / len(customers)
