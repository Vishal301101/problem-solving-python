from collections import Counter
def frequencySort(s: str) -> str:
        res = Counter(s)
        print(res)
        # count = {}
        # for char in s:
        #     count[char] = count.get(char,0) + 1
        #     print("sorted count",sorted(count))

frequencySort("tree")