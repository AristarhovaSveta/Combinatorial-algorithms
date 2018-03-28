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


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                return path + [next]
            else:
                queue.append((next, path + [next]))


if __name__ == '__main__':
    labirinth, c_start, c_end = read_labirinth()
    graph = labirinth_to_graph(labirinth)
    result = ''
    path = bfs_paths(graph, tuple(c_start), tuple(c_end))
    if path:
        result = 'Y\n' + '\n'.join([(str(x) + ' ' + str(y)) for x, y in path])
    else:
        result = 'N'
    with open('out.txt', 'w') as f:
        f.write(result)
