import math

def parse_grid(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Check if the grid is empty
    if not lines:
        return 0, 0, {}, None, []

    m, n = map(int, lines[0].strip().split(','))

    if m == 0 or n == 0:
        return m, n, {}, None, []

    # Create a dictionary to store station heights
    heights = {}
    index = 1
    for _ in range(m * n):
        height, x, y = map(int, lines[index].strip().split(','))
        heights[(x, y)] = height
        index += 1

    if index >= len(lines):
        return m, n, heights, None, []

    source = tuple(map(int, lines[index].strip().split(',')))
    index += 1

    bathhouses = []
    while index < len(lines):
        x, y = map(int, lines[index].strip().split(','))
        bathhouses.append((x, y))
        index += 1

    return m, n, heights, source, bathhouses


def build_graph(m, n, heights):
    if not heights:
        return {}

    graph = {}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for x in range(m):
        for y in range(n):
            current = (x, y)
            graph[current] = []

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    neighbor = (nx, ny)
                    if neighbor in heights:
                        height_diff = heights[neighbor] - heights[current]
                        weight = max(-1, 1 + height_diff)
                        graph[current].append((neighbor, weight))

    return graph


def optimized_bellman_ford(graph, source):
    distances = {node: math.inf for node in graph}
    distances[source] = 0
    
    relaxed = True
    for _ in range(len(graph) - 1):
        if not relaxed:  # If no relaxation occurred, exit early
            break
        relaxed = False
        for node in graph:
            for neighbor, weight in graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    relaxed = True

    return distances


memoization = {}

def find_optimal_path(graph, source, bathhouses):
    if not source or not bathhouses:
        return 0

    def set_to_key(s):
        key = 0
        for node in bathhouses:
            if node in s:
                key |= (1 << bathhouses.index(node))
        return key

    def opt(s, B):
        key = (s, set_to_key(B))

        if key in memoization:
            return memoization[key]

        if not B:
            memoization[key] = 0
            return 0

        min_cost = math.inf
        distances = optimized_bellman_ford(graph, s)

        for b in B:
            new_B = set(B)
            new_B.remove(b)

            cost = distances[b] + opt(b, new_B)
            min_cost = min(min_cost, cost)

        memoization[key] = min_cost
        return min_cost
    
    return opt(source, set(bathhouses))


def main():
    m, n, heights, source, bathhouses = parse_grid("./test_cases/TestCase10/grid.txt")

    if m == 0 or n == 0:
        print("Grid is empty.")
        return

    if not source:
        print("Source station is missing.")
        return

    if not bathhouses:
        print("No bathhouses found.")
        return

    graph = build_graph(m, n, heights)
    optimal_cost = find_optimal_path(graph, source, bathhouses)

    print("Minimum cost to visit all bathhouses:", optimal_cost)

    with open("pathLength.txt", "w") as output_file:
        output_file.write(str(optimal_cost))


if __name__ == '__main__':
    main()
