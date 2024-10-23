class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        i = 0
        n = len(s)
      
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            if result > (2**31 - 1) // 10 or (result == (2**31 - 1) // 10 and digit > 7):
                return 2**31 - 1 if sign == 1 else -2**31
            result = result * 10 + digit
            i += 1
        
        return sign * result
