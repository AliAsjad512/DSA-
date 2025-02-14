class Solution
{
    // Complete the function
    public static void deleteFromArray(int arr[], int n, int index)
    {
        // Your code here
        
        for(int i=index;i<arr.length-1;i++){
            arr[i] = arr[i+1];
            
        }
        
        arr[n-1] =0;
           
    }
}