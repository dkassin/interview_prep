from collections import defaultdict

def validPath(self, n: int, edges, source: int, destination: int) -> bool:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(i):
        if i in visited:
            return False
        if i == destination:
            return True
        visited.add(i)
        for nei in graph[i]:
            if dfs(nei):
                return True
        return False
    
    return dfs(source)