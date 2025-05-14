def solution(board):
    N = len(board)
    danger = []
    bomb = []
    
    for i in range(N):
        index_n = list(filter(lambda x: board[i][x] == 1, range(N)))
        bomb.extend([(i, x) for x in index_n])
            
    for i,j in bomb:
        danger_area = [(i+x, j+y) for x in (-1,0,1) for y in (-1,0,1)]
        danger_area = [(x,y) for x,y in danger_area if x >= 0 and x < (N)]
        danger_area = [(x,y) for x,y in danger_area if y >= 0 and y < (N)]
        danger.extend(danger_area)
        
    return (N*N)-len(set(danger))