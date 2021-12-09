import sys

input = sys.stdin.readline

def read_data():
    """
    Adapted from https://codeforces.com/blog/entry/71884
    """
    data = []
    while True:
        line = input()
        if line:
            data += [list(map(int, line.split()))]
        else:
            return data


def bfs():
    data = read_data()
    b, c = [], []
    a = data[1]
    for i in range(2, len(data)):
        b += [data[i][0]]
        c += [data[i][1]]
    data += [b, c]

    n, m, k, s, t = data[0]
    s -= 1
    t -= 1
    adj = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in a:
        adj[i-1][n] = adj[n][i-1] = 1
    for i in range(m):
        adj[b[i]-1][c[i]-1] = adj[c[i]-1][b[i]-1] = 1

    if t == s:
        return 0

    cost = 1
    visited = set()
    queue = []
    
    for i in range(n+1):
        if adj[s][i] > 0:
            if i == t:
                return cost
            else:
                queue += [i]
                visited.add(i)
    
    while queue:
        cost += 1
        len_q = len(queue)
        
        for i in range(len_q):
            for j in range(n+1):
                if adj[queue[i]][j] > 0:
                    if j == t:
                        return cost
                    elif not (j in visited):
                        queue += [j]
                        visited.add(j)

        queue = queue[len_q:]

    return -1
    

def main():
    cost = bfs()
    print(f'{cost}\n' if cost != -1 else 'Impossible\n')


if __name__ == '__main__':
    main()