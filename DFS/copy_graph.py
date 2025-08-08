from typing import Dict, List

class IntGraphNode:
    def __init__(self, value = 0, neighbors = None):
        self.value = value
        self.neighbors = neighbors if neighbors is not None else []

def copy_graph(node):
    adj_list = {}

    def dfs(node):
        nonlocal adj_list
        if node.value in adj_list:return

        adj_list[node.value] = [n.value for n in node.neighbors]

        for n in node.neighbors:
            dfs(n)
        
        if node:
            dfs(node)
        return adj_list
    
## This solves the problem on hello interview but does not solve it 
### in leetcode