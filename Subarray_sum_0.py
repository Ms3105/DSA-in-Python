def naive_sol(arr):
    n  = len(arr)
    # ret = False
    for i in range(0,n-1):
        if arr[i] == 0:
            return True
        else:
            dump = arr[i]
            # print("1",dump)
            for j in range(i+1, n):
                dump += arr[j]
                # print("2", dump)
                if dump == 0:
                    # ret= True
                    return True
    return False


def prefix_sum_array(arr):
    n = len(arr)
    Hash = set()
    # Prefix Sum Array
    PSA = [0]*n # Otherwise List out of index at PSA[i]= arr[i]
    for i in range(n):
        if i==0:
            PSA[i]= arr[i]
        else :
            PSA[i]= arr[i]+ PSA[i-1]
    for i in PSA:
        if (PSA[i] in Hash) or (PSA[i]==0):
            return True
        Hash.add(PSA[i])
    return False



arr1 = [-1, 4 , -3, -5, 6]
arr2 = [11, -11]
print(prefix_sum_array(arr1))
# print(naive_sol(arr2))
