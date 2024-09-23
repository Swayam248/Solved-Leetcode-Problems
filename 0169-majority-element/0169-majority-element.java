class Solution {
    public int majorityElement(int[] nums) {
        int candidate = nums[0];
        int count = 1;

        // Find the majority element using Boyer-Moore Voting Algorithm
        for (int i = 1; i < nums.length; i++) {
            if (count == 0) {
                candidate = nums[i];
                count = 1;
            } else if (candidate == nums[i]) {
                count++;
            } else {
                count--;
            }
        }

        return candidate;

        // Arrays.sort(nums); // Sort the array
        
        // // The majority element will occupy the middle position
        // return nums[nums.length / 2];
    }
}

