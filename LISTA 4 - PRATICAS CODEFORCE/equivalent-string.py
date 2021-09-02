def equivalent_str(str):
    if len(str) & 1: return str
    a = equivalent_str(str[ : len(str) >> 1])
    b = equivalent_str(str[len(str) >> 1 : ])
    
    return a + b if a < b else b + a
print('YES' if equivalent_str(input()) == equivalent_str(input()) else 'NO')