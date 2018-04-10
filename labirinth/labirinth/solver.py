def read_labirinth():
    with open('in.txt') as f:
        lines = f.readlines()
    rows_count = int(lines[0])
    columns_count = int(lines[1])
    coordinates_start = lines[2 + rows_count].strip().split()
    coordinates_end = lines[2 + rows_count + 1].strip().split()
    labirinth = []
    for line in lines[2:rows_count + 2]:
        labirinth.append([int(cell) for cell in line.strip().split()])
    return labirinth, [int(c) for c in coordinates_start], [int(c) for c in coordinates_end]


def labirinth_to_graph(labirinth):
    graph = {}
    for i, row in enumerate(labirinth):
        for j, cell in enumerate(row):
            if cell == 0:
                graph[(i + 1, j + 1)] = set()
                neibours = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                for x, y in neibours:
                    if (x > 0 and x < len(labirinth)) and (y > 0 and y < len(labirinth[i])):
                        if labirinth[x][y] == 0:
                            graph[i + 1, j + 1].add((x + 1, y + 1))
    return graph


def bfs(graph, start, goal):
    queue = []
    queue.append(start)
    used = {v: False for v in graph}
    d = {v: 0 for v in graph}
    p = {v: 0 for v in graph}
    used[start] = True
    p[start] = -1
    while len(queue) != 0:
        v = queue.pop(0)
        for to in graph[v]:
            if not used[to]:
                used[to] = True
                queue.append(to)
                d[to] = d[v] + 1
                p[to] = v
    with open('out.txt', 'w') as f:
        if (not used[goal]):
            f.write("N")
        else:
            f.write("Y\n")
            path = []
            v = goal
            while v != -1:
                if v != -1:
                    path.insert(0, v)
                v = p[v]
            f.write('\n'.join([str(vx) + ' ' + str(vy) for vx, vy in path]))


if __name__ == '__main__':
    labirinth, c_start, c_end = read_labirinth()
    graph = labirinth_to_graph(labirinth)
    bfs(graph, tuple(c_start), tuple(c_end))
