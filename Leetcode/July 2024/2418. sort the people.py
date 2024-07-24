class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(heights, names))
        people.sort(reverse=True, key=lambda x: x[0])
        sortednames= [name for height, name in people]
        return sortednames
