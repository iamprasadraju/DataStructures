# Insertion Sort

**Insertion sort** is a simple, in-place comparison-based sorting algorithm that builds the final sorted array one item at a time. It maintains a sorted sublist in the lower positions of the list and inserts each new item into this sublist in the correct position.

![image](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)

&nbsp; 


## Algorithm :



1. **Start with the first Element**: The first element is considered sorted.

2. **Iterate Through the Array**: For each element starting from the second:

	- Compare with Sorted Sublist: Compare the current element with elements in the sorted sublist.

	- Shift Elements: Shift elements greater than the current element to the right.

	- Insert the Element: Insert the element into its correct position in the sorted sublist.

3. **Repeat Until Sorted**: Continue until all elements are sorted.

&nbsp; 


## Implementation in Python



```python

# Insertion Sort in Python
def InsertionSort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr
```
&nbsp; 

## Complexity Analysis:

| Class                       | Sorting algorithm                       |
|----------------------------|-----------------------------------------|
| Data structure             | Array                                   |
| Worst-case performance     | O(n²) comparisons and swaps             |
| Best-case performance      | O(n) comparisons, O(1) swaps            |
| Average performance        | O(n²) comparisons and swaps             |
| Worst-case space complexity| O(n) total, O(1) auxiliary              |
| Optimal                    | No                                      |


