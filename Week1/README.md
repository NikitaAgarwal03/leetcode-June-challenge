<strong>1 June challenge</strong></br>
Invert a binary tree.

Example:
```mermaid
Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
```

<strong> 2 June challenge </strong></br>

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.</br>

Example 1:</br>

Input: head = [4,5,1,9], node = 5</br>
Output: [4,1,9]</br>
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.</br>

Example 2:</br>

Input: head = [4,5,1,9], node = 1</br>
Output: [4,5,9]</br>
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.</br>
 

Note:</br>

The linked list will have at least two elements.</br>
All of the nodes' values will be unique.</br>
The given node will not be the tail and it will always be a valid node of the linked list.</br>
Do not return anything from your function.</br>


<strong> 3 June challenge </strong></br>

There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].</br>

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.</br>


Example 1:</br>

Input: [[10,20],[30,200],[400,50],[30,20]]</br>
Output: 110</br>
Explanation: </br>
The first person goes to city A for a cost of 10.</br>
The second person goes to city A for a cost of 30.</br>
The third person goes to city B for a cost of 50.</br>
The fourth person goes to city B for a cost of 20.</br>

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.</br>
 

Note:</br>

1 <= costs.length <= 100</br>
It is guaranteed that costs.length is even.</br>
1 <= costs[i][0], costs[i][1] <= 1000</br>

<strong> 4 June challenge </strong></br>

Write a function that reverses a string. The input string is given as an array of characters char[].</br>

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.</br>

You may assume all the characters consist of printable ascii characters.</br>


Example 1:</br>

Input: ["h","e","l","l","o"]</br>
Output: ["o","l","l","e","h"]</br>

Example 2:</br>

Input: ["H","a","n","n","a","h"]</br>
Output: ["h","a","n","n","a","H"]</br>
