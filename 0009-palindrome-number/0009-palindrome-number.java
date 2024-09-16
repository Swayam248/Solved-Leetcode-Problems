class Solution {
    public boolean isPalindrome(int x) {
        int alias = x,rev=0,rem;
        if(x>0){
            while(x!=0){
                rem=x%10;
                rev=rev*10+rem;
                x=x/10;
            }
        }
        if(rev==alias){
            return true;
        }
        else{
            return false;
        }
    }
       
}