def graph_valid_tree(n, edges):
    if len(edges) != n - 1:
        return False
    
    adj_list = {i: [] for i in range(n)}
    for u,v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    visited = set()
    def dfs(adj_list,visited):
        def dfs_helper(node,parent):
            if node in visited:
                return False
            visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                if not dfs_helper(neighbor, node):
                    return False
            return True
        return dfs_helper(0,-1)
    return dfs(adj_list, visited) and len(visited) == n