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
    reds, blues = [], []
    for prop in data[1:]:
        if prop[3] == 'red':
            reds += [prop]
        else:
            blues += [prop]
    
    happy, org = dict(), dict()
    for prop in reds:
        edge = (prop[0], prop[1])
        happy[edge] = prop[2]
        org[edge] = prop[3]

    for prop in blues:
        (u, v) = (prop[0], prop[1])
        if ((u, v) not in happy) and ((v, u) not in happy):
            happy[(u, v)] = prop[2]
            org[(u, v)] = prop[3]

    A, S = [], []
    for v in range(1, n+1):
        S += [{v}]
        
    for (u, v) in sorted(happy, key=happy.get):
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

    happy_red = sum(happy[edge] for edge in A if org[edge] == 'red')
    happy_blue = sum(happy[edge] for edge in A if org[edge] == 'blue')
    print(happy_red, happy_blue, '\n')
    

if __name__ == '__main__':
    main()