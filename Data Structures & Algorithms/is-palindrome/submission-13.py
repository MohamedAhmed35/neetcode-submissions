class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [c.lower() for c in s if c.isalnum()]

        st, e = 0, len(cleaned) - 1
        while st < e:
            if cleaned[st] != cleaned[e]:
                return False

            st += 1
            e -= 1
        return True