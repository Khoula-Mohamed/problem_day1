def check(arr, n, A, B): 
     
    for i in range(A, B+1):
        a = False
        for j in range(n):
            if arr[j] == i:
                a = True
                break
        if not a:
            return False  
    return True  
 
arr = [1, 4, 5, 2, 7, 8, 3]
print('The array: ',arr)
n = len(arr)
print('check the rang of list')
A = int(input('Enter A: '))
B = int(input('Enter B: '))
if check(arr, n, A, B):
    print("YES")
else:
    print("NO!!")
    