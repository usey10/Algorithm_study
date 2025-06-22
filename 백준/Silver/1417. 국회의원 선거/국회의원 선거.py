import sys

N = int(sys.stdin.readline())

votes = {i+1 : int(sys.stdin.readline()) for i in range(N)}

max_vote = max(votes.values())
count = 0

win_vote = [k for k,v in votes.items() if v == max_vote]
while len(win_vote) != 1 or win_vote[0] != 1:
    if 1 in win_vote:
        votes[win_vote[-1]] -= 1
        votes[1] += 1
        count += 1
        max_vote = max(votes.values())
        win_vote = [k for k,v in votes.items() if v == max_vote]
    else:
        votes[win_vote[-1]] -= 1
        votes[1] += 1
        count += 1
        max_vote = max(votes.values())
        win_vote = [k for k,v in votes.items() if v == max_vote]

print(count)