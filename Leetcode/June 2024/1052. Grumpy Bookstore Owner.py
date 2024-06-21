class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        unsatisfied = sum(customer * grumpiness for customer, grumpiness in zip(customers, grumpy))
        total_customers = sum(customers)
        temp_improved = max_improved = 0
      
       
        for minute_index, (customer, grumpiness) in enumerate(zip(customers, grumpy), 1):
            temp_improved += customer * grumpiness
            if (start_index := minute_index - minutes) >= 0:
                max_improved = max(max_improved, total_customers - (unsatisfied - temp_improved))
              
                temp_improved -= customers[start_index] * grumpy[start_index]
        return max_improved     
