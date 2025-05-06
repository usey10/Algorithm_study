def solution(cipher, code):
    return ''.join(cipher[i*code-1] for i in range(1, len(cipher) // code+1))