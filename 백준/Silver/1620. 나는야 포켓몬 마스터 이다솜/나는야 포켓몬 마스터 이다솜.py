import sys

N, M = map(int, sys.stdin.readline().rstrip().split(" "))

pokemon = {i+1:sys.stdin.readline().rstrip() for i in range(N)}
reversed_pokemon = {v:k for k,v in pokemon.items()}

for _ in range(M):
    x = sys.stdin.readline().rstrip()
    if x.isdigit():
        print(pokemon.get(int(x)))
    else:
        print(reversed_pokemon.get(x))