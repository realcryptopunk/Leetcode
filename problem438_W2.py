class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        result = []
        p_freq = {}
        window_freq = {}


        for char in p:
            p_freq[char] = p_freq.get(char, 0) + 1

  
        for i in range(len(p)):
            window_freq[s[i]] = window_freq.get(s[i], 0) + 1

     
        if p_freq == window_freq:
            result.append(0)


        left = 0
        for right in range(len(p), len(s)):
            window_freq[s[right]] = window_freq.get(s[right], 0) + 1


            window_freq[s[left]] -= 1
            if window_freq[s[left]] == 0:
                del window_freq[s[left]]

            left += 1

            if p_freq == window_freq:
                result.append(left)

        return result
