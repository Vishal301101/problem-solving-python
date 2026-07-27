def canConstruct(ransomNote: str, magazine: str) -> bool:
        count = {}
        
        for char in magazine:
            count[char] = count.get(char, 0) + 1
            print("count",count)

        for char in ransomNote:
            if count.get(char, 0) == 0:
                return False       
            count[char] -= 1
            print("count",count)       

        return True

canConstruct("aa","aab")