import sys

input = sys.stdin.readline

def read_data():
    line = input()
    data = [list(map(int, line.split()))]
    while True:
        line = input()
        if line:
            line = line.split()
            line[:3] = list(map(int, line[:3]))
            data += [line]
        else:
            return data


def main():
    data = read_data()
    n, _ = data[0]
    happy_red, happy_blue = dict(), dict()
    for prop in data[1:]:
        edge = (prop[0], prop[1])
        if prop[3] == 'red':
            happy_red[edge] = prop[2]
        else:
            happy_blue[edge] = prop[2]
    
    edges_red = sorted(happy_red, key=happy_red.get, reverse=True)
    edges_blue = sorted(happy_blue, key=happy_blue.get, reverse=True)

    A, S = [], []
    for v in range(1, n+1):
        S += [{v}]
        
    for (u, v) in edges_red + edges_blue:
        for i, s in enumerate(S):
            if u in s:
                id_u = i
            if v in s:
                id_v = i

        if id_u != id_v:
            A += [(u, v)]

            if len(S[id_u]) > len(S[id_v]):
                S[id_u] = S[id_u].union(S[id_v])
                S.pop(id_v)
            else:
                S[id_v] = S[id_v].union(S[id_u])
                S.pop(id_u)

    res_red = sum(happy_red[edge] for edge in A if edge in happy_red)
    res_blue = sum(happy_blue[edge] for edge in A if edge in happy_blue)
    print(res_red, res_blue, '\n')
    

if __name__ == '__main__':
    main()