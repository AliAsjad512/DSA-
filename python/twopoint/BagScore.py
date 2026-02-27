def bagOfTokensScore(self, tokens, power):
        """
        Maximize score by playing tokens face-up (lose power, gain score)
        or face-down (gain power, lose score).
        
        Approach: Sort + two pointers (play smallest face-up, largest face-down) [citation:6]
        """

         tokens.sort()
        left, right = 0, len(tokens) - 1
        score = max_score = 0
         while left <= right:
            if power >= tokens[left]:
                # Play token face-up
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            elif score > 0:
                # Play largest token face-down
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
        
        return max_score