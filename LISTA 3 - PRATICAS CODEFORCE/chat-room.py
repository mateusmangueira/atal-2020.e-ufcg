message = 'hello'
def chat_room():
    a = input()
    b = 0
    
    for i in range(len(a)):
        if a[i] == message[b]:
            b += 1
        if b == 5:
            return ('YES')
    return ('NO')
 
print(chat_room())