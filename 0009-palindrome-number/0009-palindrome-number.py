class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        
        for i in range(0, len(x)//2,1):
            if x[i] != x[len(x) - i - 1]:
                return False
        return True
            

