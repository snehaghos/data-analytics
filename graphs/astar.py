import heapq

grid = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

start = (0, 0)
goal = (3, 3)


def heuristic(node):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


def a_star():
    queue = []
    

    heapq.heappush(queue, (heuristic(start), 0, start))

    cost = {start: 0}
    parent = {start: None}

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    while queue:
        f, g, current = heapq.heappop(queue)

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        for dx, dy in directions:
            x = current[0] + dx
            y = current[1] + dy

            if 0 <= x < 4 and 0 <= y < 4 and grid[x][y] == 0:

                new_cost = g + 1
                neighbor = (x, y)

                if neighbor not in cost or new_cost < cost[neighbor]:
                    cost[neighbor] = new_cost

                    f = new_cost + heuristic(neighbor)

                    heapq.heappush(
                        queue,
                        (f, new_cost, neighbor)
                    )

                    parent[neighbor] = current

    return None


path = a_star()

print("Shortest Path:")
print(path)

print("Path Length:", len(path) - 1)