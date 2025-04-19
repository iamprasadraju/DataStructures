# Bubbble Sort

**Bubble Sort** is a simple sorting algorithm that works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they are in the wrong order. This process is repeated until the list is sorted.

![alt text](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)


## How Bubble Sort Works:

- Start at the beginning of the array.

- Compare each pair of adjacent elements.

- if the first element is greater than the second, swap them

- Continue this process for each pair, moving the largest unsorted element to its correct position at the end of the array (like a bubble rising to the surface).

- Repeat these passes through the array until no swaps are needed, meaning the array is sorted

&nbsp; 


![![alt text](https://upload.wikimedia.org/wikipedia/commons/3/37/Bubble_sort_animation.gif)
&nbsp; 

## Code 

```python
# Bubble sort in Python

def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
```


## Complexity Analysis


| Class             | Sorting algorithm         |
|------------------|---------------------------|
| Data structure   | Array                     |
| Worst-case performance | O(n²) comparisons, O(n²) swaps |
| Best-case performance  | O(n) comparisons, O(1) swaps     |
| Average performance    | O(n²) comparisons, O(n²) swaps   |
| Worst-case space complexity | O(n) total, O(1) auxiliary |
| Optimal           | No                        |
