# Extra Task Q7
def getPairsCount(arr, n, sum):
 
    count = 0  
 
    
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
 
    return count
 
 

arr = [1,2,3,4,5,6,7,8,9,-1]
n = len(arr)
sum = 8
print("Count of pairs is",
      getPairsCount(arr, n, sum))