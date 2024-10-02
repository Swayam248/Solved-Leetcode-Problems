# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         j=-1
#         flag = 0
#         s= s.replace(" ","")
#         punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#         for ele in s:
#             if ele in s:
#                 s = s.replace(ele, "")
#         for i in range ((len(s)//2)):
#             if(s[i] == s[j]):
#                 j-=1
#                 continue
#             else:
#                 flag = 1
#                 break
#         if (flag == 0):
#             return True
#         else:
#             return False
        
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Remove all non-alphanumeric characters and convert to lowercase
        cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
        
        # Check if the cleaned string is equal to its reverse
        return cleaned_string == cleaned_string[::-1]