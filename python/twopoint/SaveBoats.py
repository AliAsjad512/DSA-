def numRescueBoats(self, people, limit):
        """
        Each boat carries at most two people with weight sum <= limit.
        
        Approach: Sort + two pointers (lightest + heaviest together if possible) [citation:9]
        """
         people.sort()
        left, right = 0, len(people) - 1
        boats = 0