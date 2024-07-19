class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        return [x] if (x:=max(min(row) for row in matrix)) == min(max(col) for col in zip(*matrix)) else []

        
