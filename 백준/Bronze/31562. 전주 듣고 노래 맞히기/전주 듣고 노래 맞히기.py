import sys

N, M = map(int, sys.stdin.readline().rstrip().split(" "))

melody = {}

for _ in range(N):
    music = sys.stdin.readline().rstrip().split(" ")
    melody[music[1]] = ''.join(music[2:5])


for _ in range(M):
    note =''.join(sys.stdin.readline().rstrip().split(" "))
    note_count = len(list(filter(lambda x: x == note, melody.values())))
    if note_count == 0:
        print("!")
    elif note_count >= 2:
        print("?")
    else:
        k = [k for k, v in melody.items() if v == note]
        print(k[0])