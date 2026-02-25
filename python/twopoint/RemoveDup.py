def removeDuplicates(self, nums):
        """
        Remove duplicates in-place from sorted array.
        
        Approach: Slow pointer for next unique position, fast for scanning
        """
        if not nums:
            return 0
        
        write_pos = 1  # Position to write next unique element
        
        for read_pos in range(1, len(nums)):
            if nums[read_pos] != nums[read_pos - 1]:
                nums[write_pos] = nums[read_pos]
                write_pos += 1
        
        return write_pos