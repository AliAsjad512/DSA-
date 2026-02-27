def bagOfTokensScore(self, tokens, power):
        """
        Maximize score by playing tokens face-up (lose power, gain score)
        or face-down (gain power, lose score).
        
        Approach: Sort + two pointers (play smallest face-up, largest face-down) [citation:6]
        """

         tokens.sort()
        left, right = 0, len(tokens) - 1
        score = max_score = 0