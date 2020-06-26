def string_compression(s: str) -> str:
    start = 0
    arr = []
    cur = s[0]
    new_str = ""

    for i in range(len(s)):
        if s[i] != cur:
            arr.append(s[start:i])
            cur = s[i]
            start = i
        if i == len(s) - 1:
            arr.append(s[start:i+1])
    
    for i in arr:
        new_str += i[0]
        new_str += str(len(i))

    return new_str


print(string_compression('aabcccccaaa'))