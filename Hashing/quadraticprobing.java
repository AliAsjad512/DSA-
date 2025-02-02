class Solution{
    //Function to fill the array elements into a hash table 
    //using Quadratic Probing to handle collisions.
    static void quadraticProbing(int[] hash, int hash_size, int arr[], int N)
    {
        //Your code here
        
        //int hash[] = new int[hash_size];
        Arrays.fill(hash,-1);
        
        for(int i=0;i<arr.length;i++){
            int key = arr[i];
            int index= key%hash_size;
            int probe=1;
            while(hash[index] !=-1 && hash[index] != key){
                index = ((key%hash_size)+ probe*probe)%hash_size;
                probe++;
                if(probe>= hash_size)
                break;
            }
            if(hash[index] == -1){
                hash[index] = arr[i];
            }
        }
        //   for(int i=0;i<hash_size;i++){
        //     System.out.print(hash[i]+" ");
        // }
      
        
        
        
    }
}



