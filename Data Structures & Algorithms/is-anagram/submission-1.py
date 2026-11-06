from typing import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1_char = defaultdict(int)
        str2_char = defaultdict(int)

        for c in s:
            str1_char[c] += 1
        
        for c in t:
            str2_char[c] += 1

        if len(s) != len(t):
            return False

        for c in s:
            if str1_char[c] != str2_char[c]:
                return False
        return True