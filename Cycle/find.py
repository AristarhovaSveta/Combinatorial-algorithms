list_of_adjacency = []
colors = {}
cycle = []


def read_from_file():
    with open('in.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    vertexes_count = int(lines[0])
    for line in lines[1:]:
        list_of_adjacency.append([int(c) - 1 for c in line.split()[:-1]])


def dfs(v, fr):
    colors[v] = 1
    for vertex in list_of_adjacency[v]:
        if colors[vertex] == 0:
            if dfs(vertex, v):
                cycle.append(vertex + 1)
                return True
        elif colors[vertex] == 1 and vertex != fr:
            cycle.append(vertex + 1)
            return True
    colors[v] = 2
    return False


def find_cycle():
    for c in range(len(list_of_adjacency)):
        if dfs(c, None):
            return True


if __name__ == '__main__':
    read_from_file()
    colors = {i: 0 for i in range(len(list_of_adjacency))}
    if find_cycle():
        result = 'N\n' + '\n'.join([str(v) for v in sorted(list(set(cycle)))])
    else:
        result = 'A'
    with open('out.txt', 'w') as f:
        f.write(result)
