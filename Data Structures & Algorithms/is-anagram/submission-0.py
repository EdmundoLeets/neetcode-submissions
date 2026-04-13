class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_s = {}
        for i in s:
            if i in freq_s:
                freq_s[i] += 1
            else:
                freq_s[i] = 1
        for j in t:
            if j in freq_s:
              freq_s[j] -= 1
              if freq_s[j] < 0:
                return False
            else:
              return False
        return True  