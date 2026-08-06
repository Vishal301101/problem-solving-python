# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

def sortCharFreq(s: str):
    count = {}
    for ch in s:
        count[ch] = count.get(ch,0)+1

    result = ""

    for ch,freq in sorted(count.items(),key=lambda x: x[1],reverse=True):
        result += ch * freq

    return result




print(sortCharFreq('tree'))