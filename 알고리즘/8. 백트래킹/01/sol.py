# 못품.
# solution
# DFS + backtracking 형태로 진행

def solution(N):
    result = []

    def dfs(path): # 리스트를 가지고 채우고 빼면서 동작
        def is_promising(path, n):
            new_i, new_j = len(path), n
            for i, j in enumerate(path):
                if new_j == j:
                    return False
                if new_i - i == abs(new_j - j):
                    return False
            return True

        if len(path) == N:
            result.append(path.copy())
            return
        
        for i in range(N):
            if is_promising(path, i):
                path += [i]
                dfs(path)
                del path[-1]
    
    dfs([])
    return result





if __name__ == '__main__':
    N = 5
    sol = solution(N)
    print(sol)
