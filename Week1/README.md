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


<strong> 5 June challenge </strong></br>
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.</br>

Note:</br>

1 <= w.length <= 10000</br>
1 <= w[i] <= 10^5</br>
pickIndex will be called at most 10000 times.</br>

Example 1:</br>

Input: </br>
["Solution","pickIndex"]</br>
[[[1]],[]]</br>
Output: [null,0]</br>

Example 2:</br>

Input: </br>
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]</br>
[[[1,3]],[],[],[],[],[]]</br>
Output: [null,0,1,1,1,0]</br>

Explanation of Input Syntax:</br>
The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.</br>


<strong> 6 June challenge </strong></br>
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.</br>

Note:</br>
The number of people is less than 1,100.</br>

Example</br>

Input:</br>
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]</br>

Output:</br>
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]</br>

<strong> 7 June challenge </strong></br>
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.</br> 

Example 1:</br>

Input: amount = 5, coins = [1, 2, 5]</br>
Output: 4</br>
Explanation: there are four ways to make up the amount:</br>
5=5</br>
5=2+2+1</br>
5=2+1+1+1</br>
5=1+1+1+1+1</br>

Example 2:</br>

Input: amount = 3, coins = [2]</br>
Output: 0</br>
Explanation: the amount of 3 cannot be made up just with coins of 2.</br>

Example 3:</br>

Input: amount = 10, coins = [10] </br>
Output: 1</br> 

Note:</br>

You can assume that</br>

0 <= amount <= 5000</br>
1 <= coin <= 5000</br>
the number of coins is less than 500</br>
the answer is guaranteed to fit into signed 32-bit integer</br>
