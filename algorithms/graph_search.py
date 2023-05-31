
from collections import deque


def breath_first_search(graph, start_vertex, target_value):
    path = [start_vertex]
    bfs_queue = deque([(start_vertex, path)])
    visited = set()

    while bfs_queue:
        current_vertex, path = bfs_queue.popleft()
        visited.add(current_vertex)

        if current_vertex == target_value:
            return path

        for neighbor in graph[current_vertex]:
            if neighbor not in visited:
                bfs_queue.append((neighbor, path + [neighbor]))

    return None