# Problem
[Delete Columns to Make Sorted II](https://leetcode.com/problems/delete-columns-to-make-sorted-ii)

We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef","vyz"].

Suppose we chose a set of deletion indices D such that after deletions, the final array has its elements in lexicographic order (A[0] <= A[1] <= A[2] ... <= A[A.length - 1]).

Return the minimum possible value of D.length.

 
Example 1:
```
Input: ["ca","bb","ac"]
Output: 1
Explanation: 
After deleting the first column, A = ["a", "b", "c"].
Now A is in lexicographic order (ie. A[0] <= A[1] <= A[2]).
We require at least 1 deletion since initially A was not in lexicographic order, so the answer is 1.
```
Example 2:
```
Input: ["xc","yb","za"]
Output: 0
Explanation: 
A is already in lexicographic order, so we don't need to delete anything.
Note that the rows of A are not necessarily in lexicographic order:
ie. it is NOT necessarily true that (A[0][0] <= A[0][1] <= ...)
```
Example 3:
```
Input: ["zyx","wvu","tsr"]
Output: 3
Explanation: 
We have to delete every column.
```

## Analysis

## Thoughts
- solution 2
  - 钻牛角尖了
  - beaware of that you only need to compare when previous row is equal 
- solution 1
  - Use x vs x+1 to compare 
  - pass by reference 
  - instead of comparing the single column, you compare multiple column **UNLESS**  deleted
    - the problem becomes for each new column, should we add it ? 
      - after we add the column, check if it is_sorted
      - python lexicographic compare: `< = >`

## Solution
- simple 
```python
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        # [c, b, a]
        def is_sorted(curr):
            return all(curr[i] <= curr[i+1] for i in range(len(A)-1))

        N = len(A[0])
        L = len(A)
        result = 0
        curr = [""] * L        
        for i in range(N):            
            pre = list(curr)
            for l in range(L):
                curr[l] += A[l][i]
            #print(curr)

            if is_sorted(curr):
                pass
            else:
                result += 1
                curr = pre
                
        return result
```

- this is with optimization
```python
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        N = len(A[0])
        result = 0
        comp_arrays = [[ i for i in range(len(A))]]
        for i in range(N):
            # for column i, check if it has a down 
            #     a   a   a   a  a  a    b
            # [ [ a , b , c , c, d, d]  [a ]]
            t = []
            print('> {}'.format(comp_arrays))
            for comp_array in comp_arrays:
                delete = False
                if len(comp_array) == 1:
                    continue
                #print(comp_array)
                for k in range(1,len(comp_array)):
                    idx = comp_array[k] 
                    if ord(A[idx][i]) - ord(A[idx-1][i])< 0:
                        # delete 
                        result += 1
                        delete = True
                        t = comp_arrays
                        #print(comp_arrays)
                        break
                
                if delete:
                    break 
            
                #  comp_array = index of [ a , b , c , c, d, d]
                # find continuous sequence [aaa b ccc] [aaaa]
                # [0,1,2] [3] [4,5,6]
                out = []
                temp = []
                pre = ''
                for idx in comp_array:
                    if pre == A[idx][i]:
                        out[-1].append(idx)
                    else:
                        out.append([idx])
                        pre = A[idx][i]
                
                # out = index of [[a] [b] [c,c] [d,d]]
                t += out

            comp_arrays = list(t)
            #print('>')
            #print(comp_arrays)
            
        return result 
```

## Tags
Greedy

## Marks
Help

[comment]: <timestamp:>