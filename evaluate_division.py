from collections import defaultdict, deque

# Rates: ['USD', 'JPY', 110] ['US', 'AUD', 1.45] ['JPY', 'GBP', 0.0070]

# adj = {usd: (jpy, 110), jpy: (usd, 1/110)}

def evaluate_division(rates: list[list[str]], conversion: list[str]) -> int:
    start, end = conversion
    adj = defaultdict(list)

    for fro, to, rate in rates:
        adj[fro].append((to, rate))
        adj[to].append((fro, 1/rate))

    q = deque()
    q.append((start, 1))
    visited = set()

    while q:
        node, rate = q.popleft()

        if node in visited:
            continue

        print(node)
    
        if node == end:
            return rate
        
        visited.add(node)

        for nigh in adj[node]:
            newNode, val = nigh
            q.append((newNode, rate*val))

    

ans = evaluate_division([['USD', 'JPY', 110], ['USD', 'AUD', 1.45], ['JPY', 'GBP', 0.0070]],['GBP', 'AUD'])
print(ans)


    

    

    
