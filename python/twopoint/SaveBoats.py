def numRescueBoats(self, people, limit):
        """
        Each boat carries at most two people with weight sum <= limit.
        
        Approach: Sort + two pointers (lightest + heaviest together if possible) [citation:9]
        """
         people.sort()
        left, right = 0, len(people) - 1
        boats = 0
         while left <= right:
            if people[left] + people[right] <= limit:
                left += 1  # Take lightest person
            right -= 1  # Always take heaviest person
            boats += 1