lass Solution
{
    //Complete the function
    public static int isSorted(int arr[], int n)
    {
        boolean ascending =true;
        boolean descending = true;
       /// Your code here
       for(int i=1;i<arr.length;i++){
           if(arr[i] < arr[i-1] )
             {
                 ascending=false;
             }
             if(arr[i] > arr[i-1] )
             {
                 descending=false;
             }
            
       }
       if(ascending || descending){
           return 1;
       }
       else{
           return 0;
       }
       
    }
}
