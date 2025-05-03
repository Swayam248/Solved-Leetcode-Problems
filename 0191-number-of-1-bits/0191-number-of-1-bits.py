class Solution:
    def hammingWeight(self, n: int) -> int:
        bin=""
        c=0
        while(n>0):
            rem = n%2
            n=n//2
            bin+=str(rem)
        for x in bin:
            if x=='1':
                c+=1
        return c