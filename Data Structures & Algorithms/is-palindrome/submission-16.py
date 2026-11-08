class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [c.lower() for c in s if c.isalnum()]

        newStr = "".join(c for c in cleaned)
        return newStr == newStr[::-1]