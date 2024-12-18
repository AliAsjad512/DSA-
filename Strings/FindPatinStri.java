



class Solution
{
    //Function to check if the given pattern exists in the given string or not.
    static boolean search(String pat, String txt)
    {
            // Your code here
            int n = txt.length();
            int m = pat.length();
            if(n < m){
                return false;
            }
            int i=0,j=0;
            while(i<n){
                if(txt.charAt(i) == pat.charAt(j)){
                    i++;
                    j++;
                   // k++;
                    if(j == m){
                        return true;
                    }
                }else{
                    i++;
                    j=0;
                   // k=0;
                    
                }
            }
            return false;
    }
    
}