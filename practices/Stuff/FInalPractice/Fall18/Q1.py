numVotes = input()
votesList = list(map(int, input().split()))
voteDict = {}

for vote in votesList:
    voteDict[vote] = voteDict.get(vote, 0) + 1

maxKey = max(voteDict, key=voteDict.get)
print(maxKey, voteDict[maxKey])
