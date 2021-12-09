import sys

input = sys.stdin.readline

class GroceryStore:

    def __init__(self, data):
        self.n, self.c, self.e, self.a, self.b = data
        self.d = [[[0 for _ in range(self.e+1)] for _ in range(self.c+1)] for _ in range(self.n+1)]
        self.fill_table()

    def fill_table(self):
        self.d[0][0][0] = 1
        for i in range(1, self.n+1):
            for j in range(self.c+1):
                for k in range(self.e+1):
                    self.fill_cell(i, j ,k)
    
    def fill_cell(self, i, j, k):
        l = j - self.a[i-1]
        m = k - self.b[i-1]
        if (l < 0) or (m < 0):
            self.d[i][j][k] = self.d[i-1][j][k]
        else:
            self.d[i][j][k] = max(self.d[i-1][j][k], self.d[i-1][l][m])

    def result(self):
        print('Yes\n' if self.d[self.n][self.c][self.e] else 'No\n') 


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


def init_store():
    data_raw = read_data()
    a, b = [], []
    data = data_raw[0]
    for i in range(1, len(data_raw)):
        a += [data_raw[i][0]]
        b += [data_raw[i][1]]
    data += [a, b]
    
    return GroceryStore(data)


if __name__ == '__main__':
    store = init_store()
    store.result()