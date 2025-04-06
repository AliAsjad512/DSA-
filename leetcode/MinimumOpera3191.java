public class MinimumOpera3191 {



    private void flipwindow(int[] nums, int pos){

    }


    public int minOperations(int[] nums){
        int n =nums.length;
        int operations =0;
        for(int i=0;i<n-2;i++){
            if(nums[i] ==1){
                continue;
            }
            flipwindow(nums, i);
            operations++;
        }

        if(nums[n-2] ==0 || nums[n-1] == 0){
            return -1
        }
return operations;
    }
    
}



