import sys

end_check = True

def d_set(d_str, d):
    if d == 0:
        str_set = set(i+j for i, j in zip(d_str[:-1], d_str[1:]))
        return str_set
    
    d_dict = {i:[] for i in range(d)}
    for idx,j in enumerate(d_str):
        d_dict[(idx+1)%d].append(j)
    str_set = set()
    for k,v in d_dict.items():
        str_set = str_set | d_set(v,0)
    return str_set


while end_check:
    check_str = sys.stdin.readline().rstrip()
    surprising = True
    if check_str == '*':
        end_check = False
        continue

    if len(check_str) <= 2:
        surprising = True
    else:
        D = len(check_str) - 2
        for i in range(D):
            str_set = d_set(check_str, i+1)
            if len(str_set) < D + 1 - i:
                surprising = False
                break
            else:
                pass
    if surprising:
        print(f'{check_str} is surprising.')
    else:
        print(f'{check_str} is NOT surprising.')