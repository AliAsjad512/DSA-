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