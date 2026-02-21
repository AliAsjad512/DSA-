def maximumScore(self, nums, k):
        """
        Find maximum score where score = min(nums[i..j]) * (j-i+1)
        and subarray must contain index k.
        
        Approach: Expand from k using two pointers
        """
        left = right = k
        min_val = nums[k]
        max_score = min_val