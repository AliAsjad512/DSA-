
// JAVA Code to count number of
// digits in an integer
import java.util.*;

class Main {

    static int countDigit(int n){
        if (n == 0)
            return 0;
        return 1 + countDigit(n / 10);
    }

    public static void main(String[] args) {
        int n = 58964;
        System.out.print(countDigit(n));
    }
}
