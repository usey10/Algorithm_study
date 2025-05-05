def solution(sides):
    max_line = sides.pop(sides.index(max(sides)))    
              
    return 1 if sum(sides) > max_line else 2