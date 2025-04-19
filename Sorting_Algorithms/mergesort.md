# Merge Sort

Merge Sort is a classic, efficient, and stable sorting algorithm based on the divide-and-conquer paradigm. It is widely used due to its predictable performance and ability to handle large datasets efficiently.


![Mergesort](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Merge-sort-example-300px.gif/250px-Merge-sort-example-300px.gif)
&nbsp; 


## How Merge Sort Works:

1. Divide:
    - The array is recursively divided into two halves until each subarray contains only one element (which is, by definition, sorted).

2. Conquer (Sort):
    - Each subarray is sorted recursively using the same merge sort algorithm.

3. Merge:
    - The sorted subarrays are then merged together to form a single sorted array. The merge step involves comparing the smallest elements of each subarray and building up the final sorted array by always taking the smaller element first 
    &nbsp; 


    ![Mergesort](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/Merge_sort_algorithm_diagram.svg/500px-Merge_sort_algorithm_diagram.svg.png)

## Code

```python
def merge_sort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves and return
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    # Compare elements from left and right lists and merge them in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements from left or right
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged
```
&nbsp;


## Complexity Analysis:

| Class                       | Sorting algorithm                          |
|----------------------------|--------------------------------------------|
| Data structure             | Array                                      |
| Worst-case performance     | O(n log n)                                 |
| Best-case performance      | Ω(n log n) typical, Ω(n) natural variant   |
| Average performance        | Θ(n log n)                                 |
| Worst-case space complexity| O(n) total with O(n) auxiliary, O(1) auxiliary with linked lists |

