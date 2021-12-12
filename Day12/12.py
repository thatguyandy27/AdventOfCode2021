input = ['pq-GX', 'GX-ah', 'mj-PI', 'ey-start', 'end-PI', 'YV-mj', 'ah-iw', 'te-GX',
         'te-mj', 'ZM-iw', 'te-PI', 'ah-ZM', 'ey-te', 'ZM-end', 'end-mj', 'te-iw',
         'te-vc', 'PI-pq', 'PI-start', 'pq-ey', 'PI-iw', 'ah-ey', 'pq-iw', 'pq-start',
         'mj-GX']

test = ['dc-end', 'HN-start', 'start-kj', 'dc-start',
        'dc-HN', 'LN-dc', 'HN-end', 'kj-sa', 'kj-HN', 'kj-dc']

test2 = ['start-A', 'start-b', 'A-c', 'A-b', 'b-d', 'A-end', 'b-end']


def parseInput(connections):
    graph = {}
    uniqueSmall = set()
    for connection in connections:
        nodes = connection.split('-')

        if nodes[0] not in graph:
            graph[nodes[0]] = []
        if nodes[1] not in graph:
            graph[nodes[1]] = []

        graph[nodes[0]].append(nodes[1])
        graph[nodes[1]].append(nodes[0])
        if nodes[0] == nodes[0].lower() and len(nodes[0]) <= 2:
            uniqueSmall.add(nodes[0])
        if nodes[1] == nodes[1].lower() and len(nodes[1]) <= 2:
            uniqueSmall.add(nodes[1])

    return graph, uniqueSmall


# Hope that there are no loops..
def dfsCount(graph, node, visited, path):
    # it is a small cave we have visited already
    if node in visited:
        return 0

    path.append(node)
    # special case end
    if node == 'end':
        print(path)
        path.pop()
        return 1
    isSmall = node == node.lower()

    if isSmall:
        visited.add(node)

    nodes = graph[node]
    count = 0

    for e in nodes:
        count += dfsCount(graph, e, visited, path)

    if isSmall:
        visited.remove(node)
    path.pop()
    return count

    # Hope that there are no loops..


def dfsCount2(graph, node, visited, path, hasVisitedSmall):
    # it is a small cave we have visited already
    if visited.get(node, 0) > 0:
        if hasVisitedSmall or node == 'start':
            return 0
        else:
            hasVisitedSmall = True

    path.append(node)
    # special case end
    if node == 'end':
        print(path)
        path.pop()
        return 1

    isSmall = node == node.lower()

    if isSmall:
        visited[node] = visited.get(node, 0) + 1

    nodes = graph[node]
    count = 0

    for e in nodes:
        count += dfsCount2(graph, e, visited, path, hasVisitedSmall)

    if isSmall:
        visited[node] = visited[node] - 1
    path.pop()
    return count


def countPaths2(input):
    graph, uniqueSmall = parseInput(input)
    return dfsCount2(graph, 'start', {}, [], False)


def countPaths(input):
    graph, uniqueSmall = parseInput(input)
    return dfsCount(graph, 'start', set(), [])


if __name__ == '__main__':
    isPart1 = False
    if isPart1:
        total = countPaths(test2)
        print('The answer is:', total)
    else:
        total = countPaths2(input)
        print('The answer is:', total)
