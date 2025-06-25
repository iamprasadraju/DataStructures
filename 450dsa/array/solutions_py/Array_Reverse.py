import random

arr = [random.randint(1, 100) for i in range(10)]
print("Actual array: ", arr)

# Using list slicing

def reverse(arr):
    return arr[::-1]

print(reverse(arr))


# -------------------------

# Using a temporary array - O(n) Time and O(n) Space

def reverseArray(arr):
    temp_arr = []

    for i in range(1, len(arr)+1):
        temp_arr.append(arr[-i])

    return temp_arr

print(reverseArray(arr))


# -------------------------


# Using Two Pointers Approach - O(n) Time and O(1) Space


def ReverseArray(arr):
    ...



# By Swapping Elements - O(n) Time and O(1) Space