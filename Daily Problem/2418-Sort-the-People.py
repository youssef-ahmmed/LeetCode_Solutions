class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = dict(zip(heights, names))
        
        sorted_people = [people[h] for h in sorted(people, reverse=True)]
        
        return sorted_people
