class Main {
    public static void main(String[] args) {
        int sizeOfArray = 6;
        int arr[] = {1, 2, 3, 4, 5};
        int copy[] = new int[sizeOfArray];
        
        int index = 2;
        int element = 90;
        
        // Copy the original array into the new array
        for (int i = 0; i < arr.length; i++) {
            copy[i] = arr[i];
        }
        
        // Shift elements to the right of the index to make space for the new element
        for (int i = sizeOfArray - 1; i > index; i--) {
            copy[i] = copy[i-1];
        }
        
        // Insert the new element at the specified index
        copy[index] = element;
        
        // Print the modified array
        for (int i = 0; i < sizeOfArray; i++) {
            System.out.print(copy[i] + " ");
        }
    }
}