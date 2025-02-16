class Solution
{
    // Complete the function
    public static int immediateGreater(int arr[], int n, int x)
    {
        Arrays.sort(arr);
        // Your code here
        int element =-1;
        for(int i=0;i<arr.length;i++){
            if(arr[i] > x){
                return arr[i];
            }
        }
        return element;
    }
}