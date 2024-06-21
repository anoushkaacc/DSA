class Solution:
    def mySqrt(self, x: int) -> int:
        low , high = 0,x
        while True:
            n = low + (high - low)//2
            if n*n <= x< (n+1)* (n+1):
                return n
            elif x < n*n:
                high = n-1
            else:
                low = n+1        


# without using any built-in or operators
