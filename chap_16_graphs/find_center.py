from collections import defaultdict

# def find_center(edges) -> int:
#     graph = defaultdict(list)
#     for x,y in edges:
#         graph[x].append(y)
#         graph[y].append(x)

#     max_val = 0
#     star = None
#     for i,j in graph.items():
#         if len(j) > max_val:
#             max_val,star = len(j),i
            
#     return star


## Better Solution

def find_center(edges) -> int:
    a,b = edges[0]
    c,d = edges[1]

    if a == c or a == d:
        return a
    else:
        return b