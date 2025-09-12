import java.util.HashMap;
import java.util.Map;

public class CharacterFrequency {
    public static void main(String[] args) {
        String text = "AABABBA";
        int k=1;
        int p1=0;
        int p2=0;
        String s2="";
        int max=0;
        int min=0;
        int window_size=0;
        int maxLength=0;
        Map<Character, Integer> charFrequencies = new HashMap<>();
        
        while(p2<text.length()){
            s2=s2+text.charAt(p2);
            window_size++;
            for (char c : s2.toCharArray()) {
            charFrequencies.put(c, charFrequencies.getOrDefault(c, 0) + 1);
        }
        for (Map.Entry<Character, Integer> entry : charFrequencies.entrySet()) {
            System.out.println("Character '" + entry.getKey() + "' appears " + entry.getValue() + " times.");
            max=Math.max(max, entry.getValue());
            min=Math.max(min, entry.getValue());
            System.out.println("Max is "+max);
             System.out.println("Min is "+min);
            
            
            if(window_size-max <=k){
                maxLength=window_size;
            }
            else{
                maxLength=maxLength-1;
                p1++;
            }
        }
        
        p2++;
        
        
        
        
            
        }
System.out.println(maxLength);
        

        
    }
}