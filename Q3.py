from collections import defaultdict

def Q3():
    n, m = input().split()
    edges = []
    m = int(m)
    n = int(n)
    for i in range(m):
        x, y = input().split()
        edges.append((x, y))

    (u, v) = input().split()
    graph = defaultdict(list)
    for edge in edges:
        a, b = edge[0], edge[1]
        graph[a].append(b)
        graph[b].append(a)
    
    distance = BFS_SP(graph, u, v)
    return distance
    

def BFS_SP(graph, start, goal):
    visited = []
    queue = [[start]]
    
    dist = 0
    if start == goal:
        return dist
    
    while queue:
        path = queue.pop(0)
        vertex = path[-1]
        
        if vertex not in visited:
            neighbors = graph[vertex]
             
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
                if neighbor == goal:
                    dist = len(new_path)-1
                    return dist
            visited.append(vertex)
 
    return -1

print(Q3())