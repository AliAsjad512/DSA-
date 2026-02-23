 def twoSumII(self, numbers, target):
        """
        Find two numbers that add up to target in a sorted array.
        Returns 1-indexed positions.
        
        Approach: Use two pointers from both ends, adjust based on sum comparison [citation:8]
        """
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]