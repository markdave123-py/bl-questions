# Imagine you’re in a wildlife center with the space around you being represented by a grid. 
# Assuming that each cell can contain one of two values, an _ representing a free spot and an X representing a tree, 
# what is the maximum distance you can see in any non-diagonal direction. 
# Note the maximum a cell can see is the sum of distances it can see in all four cardinal directions
# you can only see to the right and bottom


def dfs(grid, r, c , dr, dc, memo):

    if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0 or grid[r][c] == 'X':
        return 0
    
    if (r, c , dr, dc) in memo:
        return memo[(r, c , dr, dc)]
    
    visible = 1 + dfs(r + dr, c + dc, dr, dc, memo)

    memo[(r, c , dr, dc)] = visible

    return memo[(r, c , dr, dc)]

def max_visibility(grid):
    memo = {}
    max_v = 0
    direc = ((0,1), (1,0), (-1,0), (0, -1))
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "-":
                total = 0
                for x, y in direc:
                    total += dfs(grid, r+x, c+y, x, y, memo)

                max_v = max(max_v, total)

    return max_v

def max_visibility_dp(grid):
    n = len(grid)
    m = len(grid[0])

    # DP tables for each direction
    left  = [[0] * m for _ in range(n)]
    right = [[0] * m for _ in range(n)]
    up    = [[0] * m for _ in range(n)]
    down  = [[0] * m for _ in range(n)]

    # -------------------------
    # LEFT sweep (left → right) for each row check the colum
    # -------------------------
    for r in range(n):
        count = 0
        for c in range(m):
            if grid[r][c] == 'X':
                count = 0
            else:
                left[r][c] = count
                count += 1

    # -------------------------
    # RIGHT sweep (right → left) for each row check the column in reserved direction
    # -------------------------
    for r in range(n):
        count = 0
        for c in range(m-1, -1, -1):   # NO reversed(), just manual indices
            if grid[r][c] == 'X':
                count = 0
            else:
                right[r][c] = count
                count += 1

    # -------------------------
    # UP sweep (top → bottom) for each column check the row
    # -------------------------
    for c in range(m):
        count = 0
        for r in range(n):
            if grid[r][c] == 'X':
                count = 0
            else:
                up[r][c] = count
                count += 1

    # -------------------------
    # DOWN sweep (bottom → top), for each column check the row in reversed direction
    # -------------------------
    for c in range(m):
        count = 0
        for r in range(n-1, -1, -1):   # also no reversed()
            if grid[r][c] == 'X':
                count = 0
            else:
                down[r][c] = count
                count += 1

    # -------------------------
    # Compute max visibility
    # -------------------------
    max_view = 0
    for r in range(n):
        for c in range(m):
            if grid[r][c] == '_':      # free cell
                total = left[r][c] + right[r][c] + up[r][c] + down[r][c]
                max_view = max(max_view, total)

    return max_view
# 🔍 Step-by-Step Dry Run
# Let’s use this example grid:

# nginx
# Copy code
# _  X  _
# _  _  X
# X  _  _
# Index form:

# scss
# Copy code
# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2,2)
# ① LEFT DP Sweep (left → right)
# We count how many free cells are visible to the left.

# Row 0
# sql
# Copy code
# _   X   _
# 0   0   0   → left table row = [0, 0, 0]
# Row 1
# css
# Copy code
# _   _   X
# 0   1   0   → (1,1) sees 1 free cell to the left
# Row 2
# css
# Copy code
# X   _   _
# 0   0   1   → (2,2) sees 1 free cell to the left
# Left DP result:

# Copy code
# 0 0 0
# 0 1 0
# 0 0 1
# ② RIGHT DP Sweep (right → left)
# Count visibility to the right.

# Row 0
# nginx
# Copy code
# _   X   _
# 0   0   0
# Row 1
# scss
# Copy code
# _   _   X
# 1   0   0   → (1,0) sees (1,1)
# Row 2
# nginx
# Copy code
# X   _   _
# 0   1   0
# Right DP result:

# Copy code
# 0 0 0
# 1 0 0
# 0 1 0
# ③ UP DP Sweep (top → bottom)
# Count visibility upwards.

# Column 0:

# pgsql
# Copy code
# _      → up = 0
# _      → sees (0,0) → 1
# X      → reset to 0
# Column 1:

# nginx
# Copy code
# X  → 0
# _  → 0
# _  → 1
# Column 2:

# nginx
# Copy code
# _  → 0
# X  → 0
# _  → 0
# Up DP result:

# Copy code
# 0 0 0
# 1 0 0
# 0 1 0
# ④ DOWN DP Sweep (bottom → top)
# Count visibility downwards.

# Column 0:

# nginx
# Copy code
# X → 0
# _ → 0
# _ → 1
# Column 1:

# nginx
# Copy code
# _  → 0
# _  → 1
# X  → 0
# Column 2:

# nginx
# Copy code
# _ → 0
# X → 0
# _ → 0
# Down DP result:

# Copy code
# 0 1 0
# 0 0 0
# 0 0 0
# ⭐ FINAL VISIBILITY (sum up all 4 DP tables)
# Let’s compute visibility only for '_' cells:

# Cell	left	right	up	down	Total
# (0,0) _	0	0	0	0	0
# (0,2) _	0	0	0	0	0
# (1,0) _	0	1	1	0	2
# (1,1) _	1	0	0	1	2
# (2,1) _	0	1	1	0	2
# (2,2) _	1	0	0	0	1

# 🔥 Maximum visibility = 2
# The cells achieving 2 visibility are:

# (1,0)

# (1,1)

# (2,1)

# 🎯 Why This DP Works (in one sentence)
# Each sweep builds visibility by depending only on the previously computed cell in that direction, making it possible to compute all directional visibilities in four linear passes — achieving true O(N × M) optimal performance.
            
