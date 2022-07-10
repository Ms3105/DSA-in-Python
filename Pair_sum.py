# Naive Method O(n2), S(1)
def pair_sum(arr, targetsum):
    arr_len = len(arr)
    count =0
    for  i in range(arr_len-1):
        for j in range(i,arr_len):
            if (arr[i]+arr[j]==targetsum):
                count += 1
    
    return count
# Hashing set Method O(N), S(N)
def pair_sum1(arr, targetsum):
    hash = set()
    count = 0
    for i in arr:
        required = targetsum - i
        if required in hash:
            count += 1
        hash.add(i)
    return count
def pair_sum2(arr, target_sum):
    arr.sort()
    arrLen = len(arr)
    left = 0 
    right = arrLen-1
    count = 0
    while (left < right):
        required = arr[left]+ arr[right]
        if (required ==target_sum):
            count+=1
            left+=1
            right-=1
        elif (required > target_sum):
            right -=1
        else :
            left+=1
    return count




arr = [1, 2 ,10, 9, 11, 25]
targetsum = 11
print(pair_sum2(arr, targetsum))

