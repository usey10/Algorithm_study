import sys

N = int(sys.stdin.readline())

s_card = {"STRAWBERRY" : 0, "BANANA":0, "LIME":0, "PLUM":0}

def cardOpen(x):
    S, X = x.split(" ")
    s_card[S] += int(X)

for _ in range(N):
    s, x = sys.stdin.readline().rstrip().split(" ")
    s_card[s] += int(x)

print("YES" if 5 in set(s_card.values()) else "NO")