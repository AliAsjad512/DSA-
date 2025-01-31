

// Linear Probing in Hashing
// Difficulty: EasyAccuracy: 25.49%Submissions: 53K+Points: 2
// Linear probing is a collision-handling technique in hashing. Linear probing says that whenever a collision occurs, search for the immediate next position.

// Given an array of integers and a hash table size. Fill the array elements into a hash table using Linear Probing to handle collisions. Duplicate elements must be mapped to the same position in the hash table while colliding elements must be mapped to the [(value+1)%hashSize] position.

// Note :-  If there's no more space to insert a new element, just drop that element. 

// Example 1:

// Input:
// hashSize = 10
// sizeOfArray = 4 
// Array[] = {4,14,24,44}
// Output:
// -1 -1 -1 -1 4 14 24 44 -1 -1
// Explanation: 
// 4%10=4, So put 4 in hashtable[4].
// Now, 14%10=4, but hashtable[4] is already filled so put 14 in the next slot and so on for further elements.
// Example 2:

// Input:
// hashSize = 10
// sizeOfArray = 4 
// Array[] = {9,99,999,9999}
// Output:
// 99 999 9999 -1 -1 -1 -1 -1 -1 9
// Explanation: 
// 9%10=9, So put 9 in hashtable[9]. 
// Now, 99%10=9, but hashtable[9] is already filled so put 99 in the (99+1)%10 = 0 slot so 99 goes into hashtable[0] and so on for further elements.




class Solution{
    //Function to fill the array elements into a hash table 
    //using Linear Probing to handle collisions.
    int[] linearProbing(int hash_size, int arr[], int sizeOfArray)
    {
        //Your code here
         
        int hasharr[] = new int[hash_size];
        Arrays.fill(hasharr,-1);
        
    
    
       for(int j=0;j<sizeOfArray;j++){
           
           int key=arr[j];
           
           int index= key%hash_size;
           
           while(hasharr[index] != -1 && hasharr[index] != key){
               index = (index+1) % hash_size;
               if(index==key%hash_size)
               
               break;
           }
           
           if(hasharr[index] == -1){
               hasharr[index] = key;
              // filledSlots++;
           }
           
           
           
       }
       
       return hasharr;
        
        
        
    }
}
