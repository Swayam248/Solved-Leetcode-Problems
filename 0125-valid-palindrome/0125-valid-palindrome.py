class Solution:
    def isPalindrome(self, s: str) -> bool:
       # l=[]
        # for x in s:
        #     if x.isalnum():
        #         l.append(x.lower())
        # res = "".join(l)
        # return res == res[::-1]
        return "".join([ch for ch in s if ch.isalnum()]).lower() == "".join([ch for ch in s if ch.isalnum()]).lower()[::-1]
        # return res == res[::-1]
        # return "".join([ch for ch in s if ch.isalnum()]).lower() == "".join([ch for ch in s if ch.isalnum()]).lower()[::-1]