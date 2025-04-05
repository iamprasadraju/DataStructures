# Selection Sort

The selection sort algorithm finds the lowest value in an array and moves it to the front of the array.


![selection sort](https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif)

&nbsp; 

## Algorithm:

1. Find a largest number number in prefix A[:i + 1] and swap it to A[i]

2. Recursively sort prefix A[:i]

3. Example: [8, 2, 4, 9, 3], [8, 2, 4, 3, 9], [3, 2, 4, 8, 9], [3, 2, 4, 8, 9], [2, 3, 4, 8, 9]

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

![selectionsort](https://github.com/user-attachments/assets/a0a411b5-be6f-472a-b3ad-0327f0f9e9d9)

| **Class**                | Sorting algorithm     |
|--------------------------|-----------------------|
| **Data Structure**        | Array                 |
| **Worst-case performance**| O(n²) comparisons, O(n) swaps |
| **Best-case performance** | O(n²) comparisons, O(1) swap |
| **Average performance**   | O(n²) comparisons, O(n) swaps |
| **Worst-case space complexity** | O(1) auxiliary |
| **Optimal**               | No                    |


