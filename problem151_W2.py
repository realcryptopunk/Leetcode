class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        i = len(words) - 1
        result = ""
        while i >= 0:
            reverse = reverse + " " + words[i]
            i = i - 1
        return result.strip()

            
        
