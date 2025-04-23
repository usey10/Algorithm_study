def solution(n, w, num): 
    num_d = num - 1
    n_d = n - 1
    all_box = n_d // w
    box = num_d // w
    if box % 2 == 0:
        index = w -1 if num % w == 0 else num % w - 1
    else:
        print(num % w)
        index = 0 if num % w == 0 else w - (num % w)
    
    
    if all_box % 2 == 0:
        box_index = w-1 if n % w == 0 else (n % w) - 1
        print(all_box, box, box_index ,index)
        answer = all_box - box if index > box_index else all_box - box + 1
    else:
        box_index = 0 if n % w == 0 else w - (n % w)
        print(all_box, box, box_index ,index)
        answer = all_box - box if index < box_index else all_box - box + 1

    return answer