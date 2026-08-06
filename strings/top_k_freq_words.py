from collections import Counter
from typing import List

def topKFrequent( words: List[str],k) -> List[str]:
        word_count = Counter(words)
        if word_count.values() == k:
                return word_count.keys()
        
topKFrequent(["i","love","leetcode","i","love","coding"],2)