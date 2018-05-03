def read_from_file():
    with open('in.txt') as f:
        lines = f.readlines()
    vertex_count = int(lines[0])
    start = int(lines[1 + vertex_count])
    end = int(lines[1 + vertex_count + 1])
    matrix = []
    for line in lines[1:vertex_count + 1]:
        matrix.append([int(cell) for cell in line.strip().split()])
    return matrix, start - 1, end - 1, vertex_count


def Dijkstra(matrix, vertex_count, start, end):
    INF = 32767
    dist = [INF] * vertex_count
    prevs = [None] * vertex_count
    dist[start] = 1
    mark = [False] * vertex_count
    for i in range(vertex_count):
        v = -1
        for j in range(vertex_count):
            if (not mark[j]) and (v == -1 | dist[j] < dist[v]):
                v = j
        if dist[v] == INF:
            break
        mark[v] = True
        for j in range(len(matrix[v])):
            length = matrix[v][j]
            if dist[v] * length < dist[j]:
                dist[j] = dist[v] * length
                prevs[j] = v

    path = []
    weight = 1
    while end is not None:
        if prevs[end] is not None:
            weight *= matrix[prevs[end]][end]
        path.append(end)
        end = prevs[end]
    path = [v + 1 for v in path[::-1]]
    return path, weight


if __name__ == '__main__':
    matrix, start, end, vertex_count = read_from_file()
    path, weight = Dijkstra(matrix, vertex_count, start, end)
    with open('out.txt', 'w') as f:
        if len(path) == 1:
            f.write('N')
        else:
            f.write('\n'.join([
                'Y', ' '.join([str(v) for v in path]), str(weight)
            ]))
