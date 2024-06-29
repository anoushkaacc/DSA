class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [[] for i in range(n)]
        directchild = [[] for i in range(n)]
        for e in edges:
            directchild[e[0]].append(e[1])
        for i in range(n):
            self.dfs(i, i, ans, directchild)
        return ans
    def dfs(self, x:int, curr: int, ans: List[List[int]], directchild: List[List[int]]) -> None:
        for ch in directchild[curr]:
            if not ans[ch] or ans[ch][-1]!=x:
                ans[ch].append(x)
                self.dfs(x,ch,ans,directchild)

        
