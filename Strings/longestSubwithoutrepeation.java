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
