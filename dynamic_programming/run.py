def solve(N, K, grid):
    dp = [[float("inf")]*N for _ in range(N)]
    dist = {}
    for i in range(1, K+1):
        dist[i]=[]
    for i in range(N):
        for j in range(N):
            dist[grid[i][j]].append((i,j))
    for i in range(1, K+1):
        if len(dist[i])==0:
            return -1
        if i == 1:
            for x,y in dist[i]:
                dp[x][y]=0
                
    for i in range(2, K+1):
        for x,y in dist[i]:
            for x_p, y_p in dist[i-1]:
                largex=max(x, x_p)
                smallx=min(x, x_p)
                largey=max(y, y_p)
                smally=min(y, y_p)
                dp[x][y]=min(dp[x][y], dp[x_p][y_p]+largex+largey-smallx-smally)
    vals = []
    for x,y in dist[K]:
        vals.append(dp[x][y])
    return min(vals)

    
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    grid = []
    for i in range(N):
        line = tuple(map(int, input().split()))
        grid.append(line)
        ans = solve(N, K, grid)