
class Solution {
    // Function to rotate an array by d elements in counter-clockwise direction.
    
    static void reverse(int arr[],int start,int end){
        while(start<end){
            int temp=arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
    static void rotateArr(int arr[], int d) {
        // add your code here
        if(d>arr.length){
            d=d%arr.length;
        }
       reverse(arr,0,d-1);
       reverse(arr,d,arr.length-1);
       reverse(arr,0,arr.length-1);
    }
}


// Java program to rotate an array by
// d elements
import java.io.*;
class RotateArray {
	/*Function to left rotate arr[] of siz n by d*/
	void leftRotate(int arr[], int d, int n)
	{
		/* To handle if d >= n */
		d = d % n;
		int i, j, k, temp;
		int g_c_d = gcd(d, n);
		for (i = 0; i < g_c_d; i++) {
			/* move i-th values of blocks */
			temp = arr[i];
			j = i;
			while (true) {
				k = j + d;
				if (k >= n)
					k = k - n;
				if (k == i)
					break;
				arr[j] = arr[k];
				j = k;
			}
			arr[j] = temp;
		}
	}

	/*UTILITY FUNCTIONS*/

	/* function to print an array */
	void printArray(int arr[], int size)
	{
		int i;
		for (i = 0; i < size; i++)
			System.out.print(arr[i] + " ");
	}

	/*Function to get gcd of a and b*/
	int gcd(int a, int b)
	{
		if (b == 0)
			return a;
		else
			return gcd(b, a % b);
	}

	// Driver program to test above functions
	public static void main(String[] args)
	{
		RotateArray rotate = new RotateArray();
		int arr[] = { 1, 2, 3, 4, 5, 6, 7 };
		rotate.leftRotate(arr, 2, 7);
		rotate.printArray(arr, 7);
	}
}