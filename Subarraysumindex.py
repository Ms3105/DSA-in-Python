def subarraysumindex(arr):
    n = len(arr)
    PSA = [0]*n
    answer = []
    for i in range(n):
        if (i == 0):
            PSA[i]= arr[i]
        else:
            PSA[i]=arr[i]+PSA[i-1]
    Hash = {}
    for j in range(n):
        if PSA[j] not in Hash:
            Hash[PSA[j]] = [j]
        else:
            Hash[PSA[j]].append(j)
    for key, value in Hash.items():
        if (key==0) or (len(value)>1):
            if key ==0:
                for val in value:
                    answer.append((0,val))
                for j in range(len(value)-1):
                    for k in range(j+1, len(value)):
                        answer.append((value[j]+1, value[k]))
            else:
                for j in range(len(value)-1):
                    for k in range(j+1, len(value)):
                        answer.append((value[j]+1, value[k]))
    return answer
    


arr = [4, -4, 0, 5, -5]
print(subarraysumindex(arr))