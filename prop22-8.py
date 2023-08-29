def distSumRec(arr, n, sum, currindex, s):
    if (currindex > n):
        return
 
    if (currindex == n):
        s.add(sum)
        return
 
    distSumRec(arr, n, sum + arr[currindex], currindex+1, s)
    distSumRec(arr, n, sum, currindex+1, s)
 

def printSum(arr,n):
    s = set()
    distSumRec(arr, n, 0, 0, s)
 

    for i in s:
        print(i,end = " ")
 
if __name__ == '__main__':
    arr = [1,2]
    n = len(arr)
    printSum(arr, n)
 
