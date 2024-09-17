class Solution {
    public int findPeakElement(int[] nums) {
        // for single element, return 0
        if(nums.length == 1){
            return 0;
        }

        // for 2 elements, check which one is greater and return that index
        if(nums.length == 2){
            if(nums[0] > nums[1]){
                return 0;
            }
            else{
                return 1;
            }
        }

        //check if the first element is greater
        if(nums[0]>nums[1]){
            return 0;
        }
        
        //check if the last element is greater
        if(nums[nums.length-1] > nums[nums.length-2]){
            return nums.length-1;
        }

        //middle element check
        int c = 0;
        for(int i = 1;i<nums.length-1;i++){
            if(nums[i] > nums[i+1] && nums[i] > nums[i-1]){
                return i;
            }
        }
        return c;
    }
}

