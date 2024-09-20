import java.util.Arrays;
class Solution {
    public boolean containsDuplicate(int[] nums) {
        //  boolean val = false;
        //  for (int x=0;x<nums.length;x++){
        //      //int ele = nums[x];
        //      for(int y = x+1;y<nums.length;y++){
        //          if(nums[y]==nums[x]){
        //              val = true;
        //              break;
        //          }
        //      }
        //  }
        //  return val;
        Arrays.sort(nums);
        
        // Check adjacent elements for equality
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) {
                return true;
            }
        }
        
        return false;
    }
}