import sys

input = sys.stdin.readline

class BerlandTransport:

    def __init__(self, data):
        self.n, self.m, self.k, self.s, self.t = data[0]
        self.cost = -1
        self.adj = [[0 for _ in range(self.n+1)] for _ in range(self.n+1)]
        self.fill_adj(data[1], data[2], data[3])

    def fill_adj(self, a, b, c):
        for i in a:
            self.adj[i-1][self.n] = self.adj[self.n][i-1] = 1

        for i in range(self.m):
            self.adj[b[i]-1][c[i]-1] = self.adj[c[i]-1][b[i]-1] = 1

    def is_destination(self, city, cost):
        if city == self.t - 1:
            self.cost = cost
            return True
        else:
            return False

    def bfs(self):
        if self.t == self.s:
            self.cost = 0
            return

        cost = 1
        visited = set()
        queue = []
        
        for i in range(self.n+1):
            if self.adj[self.s-1][i] > 0:
                if self.is_destination(i, cost):
                    return
                else:
                    queue += [i]
                    visited.add(i)
            
        while queue:
            cost += 1
            len_q = len(queue)
            
            for i in range(len_q):
                for j in range(self.n+1):
                    if self.adj[queue[i]][j] > 0:
                        if self.is_destination(j, cost):
                            return
                        elif not (j in visited):
                            queue += [j]
                            visited.add(j)

            queue = queue[len_q:]

    def result(self):
        self.bfs()
        print(f'{self.cost}\n' if self.cost != -1 else 'Impossible\n')


def read_data():
    """
    Adapted from https://codeforces.com/blog/entry/71884
    """
    data_raw = []
    while True:
        line = input()
        if line:
            data_raw += [list(map(int, line.split()))]
        else:
            return data_raw


def init_transport():
    data_raw = read_data()
    b, c = [], []
    data = [data_raw[0], data_raw[1]]
    for i in range(2, len(data_raw)):
        b += [data_raw[i][0]]
        c += [data_raw[i][1]]
    data += [b, c]
    
    return BerlandTransport(data)


if __name__ == '__main__':
    transport = init_transport()
    transport.result()