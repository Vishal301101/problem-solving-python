def isAnagram(s,t):
    if len(s) != len(t):
        return False

    count = {}
    for char in s:
        count[char] = count.get(char,0) + 1 # here initially count is initialize as 0. it is default for retreiving the character count at first
        print("Count s: ",count)

    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        print("Count t",count)

    for value in count.values():
        if value != 0:
            return False

    return True

s = "anagram"
t = "nagaram"

isAnagram(s,t)

# def is_anagram(s: str,t: str):
#     return sorted(s) == sorted(t)

# print(is_anagram("anagram","nagaram"))
