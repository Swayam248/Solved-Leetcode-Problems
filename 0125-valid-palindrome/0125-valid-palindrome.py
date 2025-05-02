class Solution:
    def isPalindrome(self, s: str) -> bool:
        return "".join([ch for ch in s if ch.isalnum()]).lower() == "".join([ch for ch in s if ch.isalnum()]).lower()[::-1]
        # return res == res[::-1]