
from collections import deque

class TreeNode:
    def __init__(self, cost: int, children: list):
        self.cost = cost
        self.children = children

def min_cost(root: TreeNode):
    minimum_cost = float('inf')
    def dfs(node, cur_cost):
        nonlocal minimum_cost

        if cur_cost >= minimum_cost:
            return
        if not node.children:
            minimum_cost = min(minimum_cost, cur_cost)
            return
        for child in node.children:
            dfs(child, cur_cost+child.cost)

    dfs(root, 0)
    return minimum_cost
    
def min_cost_bfs(root):
    q = deque()
    q.append((root, root.cost))
    mini_cost = float('inf')
    while q:
        node, cur_cost = q.popleft()
        if not node.children:
            mini_cost = min(mini_cost, cur_cost)
            continue
        for child in node.children:
            q.append((child, cur_cost + child.cost))
            
    return mini_cost
        
    
    
    
    
    
    
    
    
    
            
            
    
    
            