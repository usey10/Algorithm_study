def solution(rsp):
    rsp_dic = {'0':'5', '2':'0', '5':'2'}
    return ''.join(rsp_dic[i] for i in str(rsp))