from collections import deque

def water_jug_bfs():
    jug1 = 4
    jug2 = 3
    target = 2

    queue = deque([(0, 0)])
    visited = {(0, 0)}
    parent = {}

    while queue:
        x, y = queue.popleft()

        if x == target or y == target:
            path = []

            while (x, y) != (0, 0):
                path.append((x, y))
                x, y = parent[(x, y)]

            path.append((0, 0))
            return path[::-1]

        
        states = [
            (jug1, y),                      
            (x, jug2),                       
            (0, y),                         
            (x, 0),                          

            # Pour 4L -> 3L
            (x - min(x, jug2 - y),
             y + min(x, jug2 - y)),

            # Pour 3L -> 4L
            (x + min(y, jug1 - x),
             y - min(y, jug1 - x))
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                parent[state] = (x, y)
                queue.append(state)

    return None


path = water_jug_bfs()

print("BFS Solution:")
for state in path:
    print(state)

print("\nNumber of operations:", len(path) - 1)