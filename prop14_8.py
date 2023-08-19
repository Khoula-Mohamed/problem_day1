
h = int(input('Enter number of element '))
arr = []
for i in range(h):
    d = int(input('Enter number:'))
    arr.append(d)
print(arr)
    
def leader(arr, size):
     
     max_num = arr[size-1]  
     print (max_num,end=' ')   
     for i in range( size-2, -1, -1):       
         if max_num < arr[i]:       
             print (arr[i],end=' ')
             max_num = arr[i]
       
leader(arr, len(arr))