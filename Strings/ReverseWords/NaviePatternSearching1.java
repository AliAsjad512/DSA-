package Strings.ReverseWords;

public class NaviePatternSearching1 {

    void patSearching(String txt, String pat){

        int n=pat.length();
        int m=txt.length();
        for(int i=0;i<=m-n;i++){
            int j;
            for(j=0;j<n;j++){
                if(pat.charAt(j) != txt.charAt(i+j))
                
                 break;
                
            }
                if(j==n){
                    System.out.print(i+ " ");
                }
            }
        }

    

    public static void main(String[] args) {
        NaviePatternSearching1 b= new NaviePatternSearching1();
        String txt="I love coding";
        String pat="love";
        b.patSearching(txt,pat);
    }
    
}

