class TwoPointersOpposite:
    """
    Problems where pointers start from both ends and move toward each other.
    Time Complexity: O(n) typically
    Space Complexity: O(1) typically
    """
    
    # ---------- Problem 167: Two Sum II - Input Array Is Sorted ----------
    def twoSumII(self, numbers, target):
        """
        Find two numbers that add up to target in a sorted array.
        Returns 1-indexed positions.
        
        Approach: Use two pointers from both ends, adjust based on sum comparison [citation:8]
        """
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]  # 1-indexed as per problem
            elif current_sum < target:
                left += 1  # Need larger sum, move left pointer right
            else:
                right -= 1  # Need smaller sum, move right pointer left
        
        return []  # No solution found
    