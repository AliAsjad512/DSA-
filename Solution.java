public class Solution {
    public int maxProfit(int[] prices) {


        int n=prices.length;
        int maxP=0;
               
        int p1=0;
        int p2=p1+1;
        
       
            while( p2<n){
            if (prices[p2] <= prices[p1]) {
                p1 = p2;  
            }
       
           else{
               maxP=Math.max(maxP,prices[p2] - prices[p1]);
           }
           
            
            p2++;
            
            };


        
        return maxP;
        
    }
} {
    
}
