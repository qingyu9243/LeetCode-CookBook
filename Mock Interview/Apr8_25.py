"""
Skip to:

Header Navigation
Side Navigation
Main content
HackerRank
V
Build the Subsequences
Merging Palindromes
Subarray Products
Minimum Moves
Priority Caching
Search Suggestion System
Vera
Build the Subsequences
Description
A subsequence of a string is obtained by deleting zero or more characters from the string while maintaining order. Given a string, generate an array of all subsequences sorted alphabetically ascending, omitting the empty string.

 

Example

s = "xyz"

 

Not including the empty string, the sorted subsequences are ['x', 'xy', 'xyz', 'xz', 'y', 'yz', 'z'].

 

Function Description 

Complete the function buildSubsequences in the editor below.

 

buildSubsequences has the following parameter(s):

    str s:  the string to process

 

Returns

    str[]: an array of strings comprising all subsequences of the given string sorted alphabetically, ascending.

 

Constraints

1 < length of s < 16
s is a string of distinct lowercase English alphabetic letters ascii[a-z].
 

Input Format for Custom Testing
Sample Case 0
Sample Input 0

STDIN      Function
-----      --------
ba      →   s = "ba"
 

Sample Output 0

a
b
ba
 

Explanation 0

For s = ba, there are 3 alphabetically-ordered subsequences: ['a', 'b', 'ba'].

 

Sample Case 1
Python 3
11011121314151617181920212223242526272829303132
    return ans


if __name__ == '__main__':
Line: 32 Col: 27

Input / Output

Test Cases

Console
Test case passed:

8/8

Select a test case
Test case 0
Input (stdin)
ba
Your Output (stdout)
a
b
ba
Expected Output
a
b
ba
values, ``` ``` , Prints the values to a stream, or to sys.stdout by default. sep   string inserted between values, default a space. end   string appended after the last value, default a newline. file   a file-like object (stream); defaults to the current sys.stdout. flush   whether to forcibly flush the stream., hint

"""