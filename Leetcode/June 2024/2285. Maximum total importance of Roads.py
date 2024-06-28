class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        arr = [0]*n
        for A,B in roads:
            arr[A]+=1
            arr[B]+=1
        arr.sort()
        summ = 0
        for i in range(len(arr)):
            summ+=arr[i]*(i+1)

        return summ        
        
