# Permutation Example :

# arr = [4, 2, 3] -> no.of permutations (n!)

# 3! (3 * 2 * 1)-- > [2, 4, 3], [2, 3, 4], [2, 4, 3], [4, 3, 2], [3, 4, 2], [3, 2, 4]


def permutation(arr, chosen = [], all = []) -> list:
    if len(arr) == 0:
        all.append(chosen)

    for i in range(len(arr)):
        new_arr = arr[:i] + arr[i+1:]
        permutation(new_arr, chosen + [arr[i]])
    return all

# Time Complexity --> O(n!)

def is_sorted(arr): # Function Checks Wheather the arr is sorted or not --> return Boolean
    i = 0
    condition = True
    while i < len(arr) - 1:
        if arr[i] <= arr [i + 1]:
            condition = True
            i += 1
        else:
            condition = False
            break
    return condition

# Time Complexity --> O(n)


# Implementing Permutation Sort

def PermutationSort(arr):
    for lists in permutation(arr):
        if is_sorted(lists):
            return lists

# Time Complexity --> O(n!.n)

