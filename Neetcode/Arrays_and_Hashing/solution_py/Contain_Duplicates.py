# Problem link -> https://neetcode.io/problems/duplicate-integer?list=neetcode150

arr = [1,2,3,4]

# Using Set DataStructure
def hasDuplicates(arr):
    return len(set(arr)) != len(arr)

print(hasDuplicates(arr))


# -------------------------------------------


# Using Sorting O(n) -> Time complexity

def HasDuplicates(arr):
    sort_arr = sorted(arr)
    bool = True
    for i in range(len(sort_arr) - 1):
        if sort_arr[i] == sort_arr[i+1]:
            bool = True
        else:
            bool = False
    return bool

print(HasDuplicates(arr))



