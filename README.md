# bitsort
 Sorting algorithm using bit representation to sort an array of integers or of floats.

# Author
 Keven Presseau-St-Laurent (contact@kpresseau.com)

# Description

 The algorithm starts by creating an array of strings to hold the bit representation of each number where
 the first bit represents the sign (1 = -, 0 = +). The rest of the number is represented as an unsigned int 
 for the integers, whereas floats use IEEE 754 representation. Integers are represented in the minimum amount 
 of bits to represent the biggest number + 1 (for the sign bit). Smaller integers have 0 padded in front:
                    -10, -7, -3, 0, 3, 7, 10 => 11010, 10111, 10011, 00000, 00011, 00111, 01010

 Once the bit representation array is generated, the algorithm splits negative numbers from positive numbers 
 first since absolute negative numbers need to be sorted in descending order and positive numbers in ascending order. 
 Then the algorithm recursively applies divide and conquer to sort numbers in sub-arrays by splitting 0s and 1s at each 
 bit level by swapping them approprietly. Whenever a sub-array is smaller than 2 the algorithm stops.

# Failed attempts
 1. Tried to implement using a sequential list of operations instead of recursivity. Slower
 2. Tried using a class to compare overhead. Much slower
 3. Tried using multithreading. Too much overhead. Using threads only for the first two sub-arrays
    is barely faster for n > 10000, otherwise slightly slower

# TODO
 Implement in a lower level language
 
# Example

 Say you have the previous array unsorted as follows: 3, 0, -7, -3, 10, -10, 7
 This is the following bit representation:
 ->{0   0   1   1   0   1   0}  
    0   0   0   0   1   1   0
    0   0   1   0   0   0   1
    1   0   1   1   1   1   1
    1   0   1   1   0   0   1
 After splitting negatives and positives you get:
    1   1   1   |   0   0   0   0
 ->{0   0   1}  |  {0   1   0   0}
    1   0   0   |   0   0   0   1
    1   1   1   |   0   1   1   1
    1   1   0   |   0   0   1   1
 Then, each sub-array is sorted the same way, but 1's are placed leftmost for negative numbers, and 0's
 are placed leftmost for positive numbers as such:

    1   |   1   1   |   0   0   0   |   0
    1   |   0   0   |   0   0   0   |   1
 -> 0   |  {0   1}  |  {0   1   0}  |   0
    1   |   1   1   |   0   1   1   |   1
    0   |   1   1   |   0   1   1   |   0
*Note that numbers are swapped in both the bit representation array and the original array
    1   |   1   |   1   |   0   0   |   0   |   0
    1   |   0   |   0   |   0   0   |   0   |   1
    0   |   1   |   0   |   0   0   |   1   |   0
 -> 1   |   1   |   1   |  {0   1}  |   1   |   1
    0   |   1   |   1   |   0   1   |   1   |   0

 Sorted:
    1   |   1   |   1   |   0   |   0   |   0   |   0
    1   |   0   |   0   |   0   |   0   |   0   |   1
    0   |   1   |   0   |   0   |   0   |   1   |   0
    1   |   1   |   1   |   0   |   1   |   1   |   1
    0   |   1   |   1   |   0   |   1   |   1   |   0

