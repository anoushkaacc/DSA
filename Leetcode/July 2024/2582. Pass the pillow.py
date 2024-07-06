class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        clen = (n-1)*2
        position = time %clen
        if position <n:
            return position+1
        else:
            return 2*n-position-1  
