class Solution {
    public int[] twoSum(int[] nums, int target) {
        int k=0;
        int [] newAr=new int[2];
        for(int i=0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){
                if((nums[i]+nums[j])==target){
                    newAr[k++]=i;
                    newAr[k++]=j;
                }
            }
        }
        return newAr;
    }
}