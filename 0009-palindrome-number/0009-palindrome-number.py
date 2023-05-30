class Solution:
    def isPalindrome(self, x: int) -> bool:
        digits = list()
        y = x
        while x / 10 > 0:
            last_digit = x % 10
            x = x // 10
            digits.append(last_digit)
        

        
        initial = pow(10, len(digits) - 1)
        sum = 0
        for item in digits:
            sum += int(item * initial)
            initial /= 10
        if sum == y:
            return True
        else:
            return False

        
            

