// class Solution {
//     public int findPeakElement(int[] nums) {
//         int c = 0;
//         for(int i = 1;i<nums.length-1;i++){
//             if(nums.length == 2){
//                 if(nums[i] > nums[i-1]){
//                     c=i;
//                     break;
//                 }
//                 else{
//                     c=i-1;
//                     break;
//                 }
//             }
//             else if (nums[i] > nums[i+1] && nums[i] > nums[i-1]){
//                 c = i;
//             }
//             else{
//                 return 0;
//             }
//         }
//         return c;
//     }
// }

class Solution {
    public int findPeakElement(int[] nums) {
        // Handle the case when there's only one element or two elements
        if (nums.length == 1) {
            return 0;
        }
        if (nums.length == 2) {
            return nums[0] > nums[1] ? 0 : 1;
        }
        
        int c = 0;
        // Check if the first or last element is the peak
        if (nums[0] > nums[1]) {
            return 0;
        }
        if (nums[nums.length - 1] > nums[nums.length - 2]) {
            return nums.length - 1;
        }

        // Check for peak elements in the middle of the array
        for (int i = 1; i < nums.length - 1; i++) {
            if (nums[i] > nums[i - 1] && nums[i] > nums[i + 1]) {
                return i;
            }
        }

        // Return 0 if no peak is found, this line is unreachable with the current logic
        return c;
    }
}
