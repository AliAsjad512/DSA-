class CountingPairs:
    """
    Problems requiring counting pairs satisfying certain conditions.
    """
    
    # ---------- Problem 2563: Count the Number of Fair Pairs ----------
    def countFairPairs(self, nums, lower, upper):
        """
        Count pairs (i, j) with i < j where lower <= nums[i] + nums[j] <= upper.
        
        Approach: Sort + two pointers to count pairs <= upper and < lower [citation:3]
        """
        nums.sort()
        n = len(nums)
        def count_pairs(limit):
            """Count pairs with sum <= limit"""
            left, right = 0, n - 1
            count = 0
            
            while left < right:
                if nums[left] + nums[right] <= limit:
                    count += right - left
                    left += 1
                else:
                    right -= 1
            
            return count
        
         return count_pairs(upper) - count_pairs(lower - 1)