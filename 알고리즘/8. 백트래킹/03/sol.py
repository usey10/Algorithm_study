# solution
def solution(s):
    result = []

    def dfs(path): 
        if len(path) == 3: # 종료조건
            result.append(make_address(path))
            return
        for i in range(1,4): # 123 이터레이션
            if is_promising(path, i):
                path += [i]
                dfs(path)
                del path[-1]

    def is_promising(path, k):
        # print(s, path, k) # 디버깅
        tokens = []
        # path 가 비어있는 경우
        if not path:
            tokens.append(s[:k])
        elif len(path) == 1:
            start = path[0]
            tokens.append(s[start:start+k])
        # path 가 2인 경우 두개의 숫자를 다 확인해야함.
        else:
            start = sum(path)
            tokens.append(s[start:start+k])
            tokens.append(s[start+k:])

        # print(tokens) # 숫자가 처음에 두개가 뽑히는 경우 발생
        # print()
        for token in tokens:
            if len(token) == 0:
                return False
            if len(token) > 1 and token[0] == '0':
                return False
            if int(token) > 255:
                return False
        return True
    
    def make_address(path):
        tokens = []
        tokens.append(s[:path[0]])
        tokens.append(s[path[0]:path[0]+path[1]])
        tokens.append(s[path[0]+path[1]:path[0]+path[1]+path[2]])
        tokens.append(s[path[0]+path[1]+path[2]:])
        return '.'.join(tokens)


    dfs([])
    return result


if __name__ == '__main__':
    s = "11011"
    sol = solution(s)
    print(sol)
