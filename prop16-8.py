def sub(s):
    
    answar, lower, upper = 0, 0, 0
    for i in range(len(s)):
        upper = 0
        lower = 0
 
        for j in range(i, len(s)):
            if s[j].isupper():
                upper += 1
            else:
                lower += 1
            if upper == lower:
                answar += 1
 
    return answar

s = "WomensDAY"
print(sub(s))
print(s.isupper())