 class Solution {
     public int searchInsert(int[] nums, int target) {
//         int ans=0;
//         for (int x=0;x<nums.length;x++){
//             if (target == nums[x]){
//                 ans= x;
//                 break;
//             }
//             else if(target==0){
//                 ans= 0;
//                 break;
//             }
//             else if(nums[x] == target+1){
//                 ans= x;
//                 break;
//             }
//             else if(x==nums.length-1){
//                 ans=x+1;
//                 break;
//             }
//             else{
                
//             }
//         }
//         return ans;
        int left = 0;
        int right = nums.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        // If the target is not found, return the index where it should be inserted
        return left;
     }
 }