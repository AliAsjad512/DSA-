class Solution {
    public int characterReplacement(String s, int k) {
        

int p1 = 0; 
        int maxCount = 0; 
        int maxLength = 0; 
        
        Map<Character, Integer> freq = new HashMap<>();
        
        for (int p2 = 0; p2 < s.length(); p2++) {
            char c = s.charAt(p2);
            freq.put(c, freq.getOrDefault(c, 0) + 1);
            
            
            maxCount = Math.max(maxCount, freq.get(c));
            
            
            while ((p2 - p1 + 1) - maxCount > k) {
                char leftChar = s.charAt(p1);
                freq.put(leftChar, freq.get(leftChar) - 1);
                p1++;
            }
            
            
            maxLength = Math.max(maxLength, p2 - p1 + 1);
        }

       return maxLength;





        
    }
}



// Online Java Compiler
// Use this editor to write, compile and run your Java code online

class Main {
    public static void main(String[] args) {
       // System.out.println("Try programiz.pro");
       int[] prices = {2,1,4};
       int n=prices.length;
        int maxP=0;
               // int CurrStock=prices[0];
        int p1=0;
        int p2=0;
        while(p1<n && p2<n){
            if(prices[p2] - prices[p1] <0){
                if(p2 <n-1){
                p1++;
                p2++;
                }
            }
             else if(prices[p2] > prices[p1]){
                 System.out.println(prices[p2]);
                 int result = prices[p2] - prices[p1];
             
                maxP=Math.max(maxP,result);
            }
            else{
                p1=p2;
            
            }
           
            
            p2++;
            
            
        }
     //System.out.println(p1);
        
        
        System.out.println(maxP);
       
       
       
       
    }
}