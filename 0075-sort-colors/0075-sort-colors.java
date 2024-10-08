class Solution {
    public void sortColors(int[] nums) {
        int [] arr = new int[3];
        for(int num : nums){
            arr[num]++;
        }  // if nums = {1,0,2,2,1,0,0,0,1}, arr will be{4,3,2} 4 is the count of 0, likewise for 1 and 2

        int ind = 0;
        for(int i = 0; i<3 ;i++){
            for(int j = 0;j<arr[i];j++){
                nums[ind++] = i; // over writing on nums acc to the count in arr, 
                //{0,0,0,0,1,1,1,2,2}
            }
        }
    }
}