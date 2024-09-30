class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # x=0
        # gl = list(s)
        # l=[]
        # for i in t:
        #     if i in s:
        #         l.append(i)
        #         x+=1
        #         continue
        # if len(s) == x and l == gl:
        #     return True
        # else:
        #     return False
            # Pointers for s and t
        i, j = 0, 0
    
    # Iterate over t
        while i < len(s) and j < len(t):
        # If characters match, move the pointer of s forward
            if s[i] == t[j]:
                i += 1
        # Always move the pointer of t forward
            j += 1
    
    # If we have traversed all characters of s, return True
        return i == len(s)
            
        