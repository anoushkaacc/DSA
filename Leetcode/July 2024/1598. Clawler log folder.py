class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level=0
        for dir in logs:
            if dir =="../": level-=(level>0)
            elif dir!="./": level+=1
        return level    
        
