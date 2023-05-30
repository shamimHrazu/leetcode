class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        digits = list()
        y = x
        while x / 10 > 0:
            last_digit = x % 10
            x = x // 10
            digits.append(last_digit)
        
        
        for i in range (0, len(digits)//2, 1):
            last = len(digits) -i -1
            if digits[i] != digits[last]:
                return False
        return True
            

