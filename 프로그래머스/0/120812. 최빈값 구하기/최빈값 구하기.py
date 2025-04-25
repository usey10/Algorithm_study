def solution(array):
    if len(set(array)) == 1:
        return array[0]
    
    count = {i:0 for i in set(array)}
    for i in array:
        count[i] += 1
        
    sorted_c = sorted(count.items(), key=lambda x: x[1], reverse=True)
    print(sorted_c)
    
    if sorted_c[0][1] == sorted_c[1][1]:
        return -1
    return sorted_c[0][0]