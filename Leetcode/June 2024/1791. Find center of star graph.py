class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge1 , edge2 = edges[:2]
        return [element for element in edge1 if element in edge2] [0]
