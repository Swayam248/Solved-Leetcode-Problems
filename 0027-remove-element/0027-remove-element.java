class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0; // Pointer for indicating the position to place the next non-equal element
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[k++] = nums[i]; // Move non-equal element to position indicated by k and increment k
            }
        }
        
        return k; // k represents the count of non-equal elements
    }
}