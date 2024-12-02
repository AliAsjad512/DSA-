package Strings.Subsequnce;

public class isSubsequence {
    public static boolean isSubSequence(String A, String B)
    {
        //code here
    int p1=0;
    int p2=0;
          
            
            while(p2 < B.length() && p1 < A.length()){
                if(A.charAt(p1)==B.charAt(p2)){
                    
                
                
                  p1++;
                  //p2++;
                }
               
                 p2++;     
                   
            }
           
        
        if(p1==A.length()){
            return true;
        }
        else{
        return false;
        }
    }
    public static void main(String[] args) {
        String A="ABC";
        String B="YAXDD";
        isSubSequence(A, B);

    }
}
