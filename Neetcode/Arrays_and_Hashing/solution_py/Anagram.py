# Problem link -> https://leetcode.com/problems/valid-anagram/description/

from collections import Counter


s = "anagram"
t = "nagaram"

# Using list and Sorting 
def isAnagram(s: str, t: str) -> bool:
    s_list = sorted(list(s))
    t_list = sorted(list(t))

    return s_list == t_list

print("Method - 1:", isAnagram(s, t))

# -----------------------------

# using Dictionaries -> Most Efficient

def IsAnagram(s: str, t :str) -> bool:
    if len(s) != len(t):
        return False
    chars_s = {}
    chars_t = {}

    for i, j in zip(s, t):
       chars_s[i] = chars_s.get(i, 0) + 1
       chars_t[j] = chars_t.get(j, 0) + 1

    return chars_s == chars_t

print("Method - 2:", IsAnagram(s, t))


# --------------------------------------------


# Using Counter method from Collections

def isanagram(s : str, t : str) -> bool:
    return Counter(s) == Counter(t)


print("Method - 3:", isanagram(s, t))


# ----------------------------------------------


# Using String replace method()

def ISanagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    for i in s:
        if i in t:
            t = t.replace(i, "", 1)

    return len(t) == 0

print("Method - 4:", ISanagram(s, t))


#

def ISAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count = {}
    for a, b in zip(s, t):
        count[a] = count.get(a, 0) + 1
        count[b] = count.get(b, 0) - 1

    return all(v == 0 for v in count.values())


print("Method - 5:", ISAnagram(s, t))