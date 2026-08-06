def firstUniqueCharacter(s: str):
    count = {}
    for ch in s:
        count[ch] = count.get(ch,0) + 1
        # print("count is: ",count)

    for i,ch in enumerate(s):
        if count[ch] == 1:
            return i

    return -1

print(firstUniqueCharacter('loveleetcode'))
