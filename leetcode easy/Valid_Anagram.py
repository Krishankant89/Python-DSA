class Solution:
    
    def isAnagram(self, s:str, t:str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s = sorted(s)
        t = sorted(t)
        
        return s == t
    
if __name__ == "__main__":
    s = "racecar"
    t = "carrace"
    solution = Solution()
    
    if(solution.isAnagram(s,t)):
        print("True")
    else:
        print("False")