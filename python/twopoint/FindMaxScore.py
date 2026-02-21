def maximumScore(self, nums, k):
        """
        Find maximum score where score = min(nums[i..j]) * (j-i+1)
        and subarray must contain index k.
        
        Approach: Expand from k using two pointers
        """
        left = right = k
        min_val = nums[k]
        max_score = min_val

        while left > 0 or right < len(nums) - 1:
            # Expand in direction of larger value
            if left == 0:
                right += 1
                min_val = min(min_val, nums[right])
            elif right == len(nums) - 1:
                left -= 1
                min_val = min(min_val, nums[left])
            elif nums[left - 1] > nums[right + 1]:
                left -= 1
                min_val = min(min_val, nums[left])
            else:
                right += 1
                min_val = min(min_val, nums[right])
            
            max_score = max(max_score, min_val * (right - left + 1))