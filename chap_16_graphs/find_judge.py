from collections import defaultdict, Counter

def findJudge(n: int, trust)  -> int:
    graph = defaultdict(list)
    for u,v in trust:
        graph[u].append(v)

    trusts = Counter()
    trusted_by_someone = Counter()
    for x,y in graph.items():
        trusts[x] += len(y)
        for z in y:
            trusted_by_someone[z] += 1

    candidates = [key for key,value in trusted_by_someone.items() if value == (n-1)]
    for person in candidates:
        if person not in trusts:
            return person
        
    if n == 1 and not trust:
        return 1
    
    return -1
