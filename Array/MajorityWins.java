// Online Java Compiler
// Use this editor to write, compile and run your Java code online

class Main {
    
    public int majorityWins(int arr[], int n, int x, int y) {
       // code here
       int countX=0;
       int countY=0;
       int min=0;
       for(int i=0;i<arr.length;i++){
           if(arr[i]>=x && arr[i] == x){
               countX++;
           }
           else if( arr[i]<=y && arr[i] == y){
               countY++;
           }
       }
       
       if(countX>countY){
           return x;
       }
       else if(countX == countY){
            min = Math.min(x,y);
           return min;
       }
       
           return y;
       
       
       
   }
   public static void main(String[] args) {
      // System.out.println("Try programiz.pro");
      int n=11;
      int arr[] = {1,1,2,2,3,3,4,4,4,4,5};
      int x=4;
      int y=5;
      Main obj = new Main();
   
   int result = obj.majorityWins(arr, n, x, y);
   System.out.println(result);
      
   }
}