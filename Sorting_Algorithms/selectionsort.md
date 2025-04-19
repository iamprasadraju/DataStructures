# Selection Sort

Selection sort is a simple, comparison-based sorting algorithm that organizes a list by repeatedly finding the minimum (or maximum) element from the unsorted portion and moving it to the sorted portion.


![selection sort](https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif)

&nbsp; 

## How Selection Sort Works:

- The array is divided into two parts: a sorted subarray (initially empty) and an unsorted subarray (initially the entire array).

- On each pass, the algorithm:

	- Scans the unsorted part to find the minimum element.

	- Swaps this minimum element with the first unsorted element, effectively growing the sorted part by one and shrinking the unsorted part.


This process is repeated until all elements are sorted.

&nbsp; 


## Implementation in python


```python
	
def SelectionSort(arr, ascending = True):
	for i in range(len(arr)):
		index = i
		for j in range(i + 1, len(arr)):
			if ascending: 
				if arr[j] < arr[index]:
					index = j
			else:
				if arr[j] > arr[index]:
					index = j

		arr[i], arr[index] = arr[index], arr[i]
	return arr


```

&nbsp; 


## Complexity:

![selectionsort](https://github.com/user-attachments/assets/4eaf5079-85c5-43dd-a971-fc49e38f34d2)


| **Class**                | Sorting algorithm     |
|--------------------------|-----------------------|
| **Data Structure**        | Array                 |
| **Worst-case performance**| O(n²) comparisons, O(n) swaps |
| **Best-case performance** | O(n²) comparisons, O(1) swap |
| **Average performance**   | O(n²) comparisons, O(n) swaps |
| **Worst-case space complexity** | O(1) auxiliary |
| **Optimal**               | No                    |


