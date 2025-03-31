# solution
# team sort 가 stable 한지 물어보고, 구현하는 걸 물어보는 문제
# tuple 입력 -> 첫번쨰 값 -> 두번째 값 -> 세번쨰 값 으로 정렬
def solution(grade, class_name, score):
    # 정렬 기준 3개 + 원하는 값
    # items = [(grade[i], class_name[i], -score[i], score[i]) for i in range(len(grade))]
    items = [(g,c,-s,s) for g,c,s in zip(grade, class_name, score)]
    items.sort()
    return list(map(lambda x: x[-1], items))
    # print(items)


if __name__ == '__main__':
    grade = [3, 2, 1, 2, 1, 3, 2]
    class_name = [1, 3, 2, 3, 1, 3, 3]
    score = [50, 40, 66, 80, 100, 42, 99]
    sol = solution(grade, class_name, score)
    print(sol)
