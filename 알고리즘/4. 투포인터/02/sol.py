# def solution(ingredients, items):
#     len(items)
#     gettems = [0 for _ in range(len(ingredients))]
#     start = 0
#     end = 0
#     for i in range(len(items)):
#         if items[i] in ingredients:
#             for j in range(len(ingredients)):
#                 if ingredients[j] == items[i]:
#                     gettems[j] = 1
#     print(gettems)

# 생각해야 하는 부분 -> 아예 item이 다 들어갈 수 있는지 여부에 따라 점차 늘려나가는 방법으로 생각할 수 있음.
# 하나 하나 검사하려고 안해도 됨.
# 전체 알고리즘이 O(N²) 이 되므로 최적화 필요 -> 딕셔너리로 변경

# solution
def solution(ingredients, items):
    buy_dict = dict() # 딕셔너리로 최적화
    left, right = 0, 0
    result = len(items)

    set_a = set(ingredients)
    buy_dict[items[left]] = 1
    # set_b = set(items[left:right+1]) # O(N)
    # if set_a.issubset(set_b):
    if set_a.issubset(buy_dict.keys()):
        result = 1
        return result
    
    while left <= right: # O(N)
        # set_b = set(items[left:right+1]) 
        # if set_a.issubset(set_b):
        if set_a.issubset(buy_dict.keys()):
            result = min(result, right - left + 1)
            
            if buy_dict[items[left]] == 1:
                del buy_dict[items[left]]
            else:
                buy_dict[items[left]] -= 1

            left += 1
        else:
            right += 1

            if right == len(items):
                break

            if items[right] in buy_dict:
                buy_dict[items[right]] += 1
            else:
                buy_dict[items[right]] = 1

    return result


if __name__ == '__main__':
    ingredients = ["생닭", "인삼", "소주", "대추"]
    items = ["물", "인삼", "커피", "생닭", "소주", "사탕", "생닭", "대추", "쌀"]
    sol = solution(ingredients, items)
    print(sol)
