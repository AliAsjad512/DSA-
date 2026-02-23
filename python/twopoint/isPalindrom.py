 def isPalindrome(self, s):
        """
        Check if string is palindrome considering only alphanumeric chars.
        
        Approach: Two pointers from ends, skip non-alphanumeric [citation:2][citation:6]
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters from left
            while left < right and not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric characters from right
            while left < right and not s[right].isalnum():
                right -= 1