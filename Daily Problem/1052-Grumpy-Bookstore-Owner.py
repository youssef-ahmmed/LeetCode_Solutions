class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        staisfied_customers = 0

        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                staisfied_customers += customers[i]

        mx_owner = 0
        sum_period = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 1:
                sum_period += customers[i]
    
            if i >= minutes - 1:
                mx_owner = max(mx_owner, sum_period)
                if grumpy[i - minutes + 1] == 1:
                    sum_period -= customers[i - minutes + 1]            
        
        staisfied_customers += mx_owner

        return staisfied_customers
