 def moveZeroes(self, nums):
        """
        Move all zeros to end while maintaining relative order of non-zero elements.
        
        Approach: Slow pointer tracks position for next non-zero
        """
        non_zero_pos = 0
        
        # Move all non-zero elements to front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_pos], nums[i] = nums[i], nums[non_zero_pos]
                non_zero_pos += 1
        # Remaining elements are already zero, no need to fill explicitly   
        