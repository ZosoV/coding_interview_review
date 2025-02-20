# Big Os

- `O(1)` Constant- no loops
- `O(log N)` Logarithmic- usually searching algorithms have log n if they are sorted (Binary Search)
    - Each step reduces the input size by a factor (e.g., half), leading to a logarithmic number of operations.
    - Examples: Binary search, balanced tree traversals
- `O(n)` Linear- for loops, while loops through n items
- `O(n log(n))` Log Liniear- usually sorting operations
    - Examples: Merge Sort, Quick Sort (average case), Heap Sort.
- `O(n^2)` Quadratic- every element in a collection needs to be compared to ever other element. Two nested loops
    - Examples: Bubble sort, selection sort, insertion sort, brute-force comparison of all pairs
- `O(2^n)` Exponential- recursive algorithms that solves a problem of size N
    - It typically occurs when each function call branches into two recursive calls, leading to 2^n operations.
    - Examples: Fibonacci using naïve recursion, subsets generation, combinatorial problems
- `O(n!)` Factorial- you are adding a loop for every element
    - Brute-force permutations or combinatorial problems
    - Example: Generating all possible orderings of n elements (e.g., Traveling Salesman Problem using brute-force).


- **Iterating through half a collection is still** `O(n)`
- **Two separate collections:** `O(a * b)`

### **What can cause time in a function?**

    Operations (+,-,*,/)
    Comparisons (<,>,==)
    Looping (for, while)
    Outside Function call (function())

### Rule Book

- **Rule 1**: Always worst Case
- **Rule 2**: Remove Constants
- **Rule 3**: 
    - Different inputs sould have diferent variables. `O(a+b)`. 
    - A and B arrays nested would be `O(a*b)`.
        - for steps in order +
        - for nested steps *
- **Rule 4:** Drop Non-dominant terms

### What causes Space Complexity?

    Variables
    Data Structures
    Function Call
    Allocations

### Check also these links

- [https://www.bigocheatsheet.com/](https://www.bigocheatsheet.com/)
