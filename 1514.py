#Uri Questions
#Python
#Competição
while True:
    n,m = map(int, input().split())
    if n == m == 0: break;
    players = []
    ok = 4
    for x in range(n):
        players.append(input().split())
    for read in players:
        if read.count('1') == m:
            ok -= 1
            break
    for p in range(m):
        hai = 0
        for pp in range(len(players)):
            if players[pp][p] == '0':
                hai += 1
        if hai == n:
            ok -= 1
            break
    for p in range(m):
        hai = 0
        for pp in range(len(players)):
            if players[pp][p] == '1':
                hai += 1
        if hai == n:
            ok -= 1
            break
    for read in players:
        if read.count('0') == m:
            ok -= 1
