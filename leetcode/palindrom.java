// LeetCode Problem: Palindrome Number
// Determine whether an integer is a palindrome.
// An integer is a palindrome when it reads the same backward as forward.

function isPalindrome(x) {
  if (x < 0) return false; // Negative numbers can't be palindrome

  let original = x;
  let reversed = 0;

  while (x > 0) {
    reversed = reversed * 10 + (x % 10);
    x = Math.floor(x / 10);
  }

  return original === reversed;
}

// Example usage
console.log(isPalindrome(121));  // true
console.log(isPalindrome(-121)); // false
console.log(isPalindrome(10));   // false
