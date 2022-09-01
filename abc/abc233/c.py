N, X = map(int, input().split())

an = [list(map(int, input().split()))[1:] for _ in range(N)]

ans = 0
def bfs(idx, prod):
    global ans
    # print("call : bfs({}, {})".format(idx, prod))
    if prod > X:
        # print("call : bfs({}, {})".format(idx, prod))
        # print("cut")
        return False

    if idx == N:
        if prod == X:
            ans += 1
        else:
            pass
        return False


    for i in an[idx]:
        bfs(idx+1, prod*i)
        
bfs(0, 1)
print(ans)

