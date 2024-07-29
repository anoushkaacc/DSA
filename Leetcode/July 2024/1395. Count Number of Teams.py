class Solution:
    def numTeams(self, rating: List[int]) -> int:
        t = 0
        n = len(rating)
        for i in range(n):
            rl=0
            rm=0
            ll=0
            lm=0

            for j in range(i+1,n):
                if rating[j] < rating[i]:
                    rl+=1
                elif rating[j]>rating[i]:
                    rm+=1
            
            for j in range(i):
                if rating[j]<=rating[i]:
                    ll+=1
                elif rating[j]>rating[i]:
                    lm+=1
                
            t += rl*lm + rm*ll
        return t
        
