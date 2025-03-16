import java.util.*;

class FibonacciPasswordGenerator {
    
    // Function to generate Fibonacci sequence up to n terms
    public static List<Integer> generateFibonacci(int n) {
        List<Integer> fibList = new ArrayList<>();
        if (n <= 0) return fibList;
        
        fibList.add(0);
        if (n == 1) return fibList;
        
        fibList.add(1);
        for (int i = 2; i < n; i++) {
            fibList.add(fibList.get(i - 1) + fibList.get(i - 2));
        }
        return fibList;
    }

    // Function to convert Fibonacci numbers into a password
    public static String generatePassword(int length) {
        List<Integer> fibList = generateFibonacci(length);
        
        String characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*";
        StringBuilder password = new StringBuilder();

        for (int num : fibList) {
            
            int index = num % characters.length(); // Ensure it's within bounds
            password.append(characters.charAt(index));
        }

        return password.toString();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the password length (min 5): ");
        int length = scanner.nextInt();

        if (length < 5) {
            System.out.println("Password length should be at least 5.");
        } else {
            String password = generatePassword(length);
            System.out.println("Generated Fibonacci-Based Password: " + password);
        }
        
        scanner.close();
    }
}
