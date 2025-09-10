public class longestSubwithoutrepeation {

    String s= "dvdf";
    int n = s.length();
    int maxi=0;
    for(int i=0;i<n;i++){
        for(int j=i;j<n;j++){
            if(allUnique(s,i,j)){
                maxi=Math.max(maxi,j-i+1);
            }
        }
    }
    
}

public static boolean allUnique(String s, int start, int end){
    for(int i=start; i<=end ;i++){
        for(int j=i+1; j<=end;j++){
            if(s.charAt(i) == s.charAt(j)){
                return false;
            }
        }
    }
    return true;
}
