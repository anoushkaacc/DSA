class Solution:
    def fn(self, p, m, mid):
        cnt = 1
        prev = p[0]
        for i in range(1, len(p)):
            if p[i] - prev >= mid:
                cnt += 1
                prev = p[i]
        return cnt >= m

    def maxDistance(self, p, m):
        p.sort()
        lo = 1
        hi = p[-1] - p[0]
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if self.fn(p, m, mid):
                lo = mid
            else:
                hi = mid - 1
        if self.fn(p, m, hi):
            return hi
        return lo
        
