class QueryMutable:
    def __init__(self, matrix):
        self.matrix = matrix
        self.col = len(matrix[0])
        self.row = len(matrix)
        self.grid = [[0] * self.col for _ in range(self.row)]
        self.BIT = [[0] * (self.col + 1) for _ in range(self.row + 1)]

        for i in range(self.row):
            for j in range(self.col):
                self._update(i, j, self.matrix[i][j])

    def _update(self, r, c, val):
        newVal = val - self.grid[r][c]
        self.grid[r][c] = val

        i = r + 1
        while i <= self.row:
            j = c + 1

            while j <= self.col:
                self.BIT[i][j] += newVal
                j += j & -j
            i += i & -i

    def _sum(self, r, c):
        total = 0

        i = r + 1
        while i > 0:
            j = c + 1
            while j > 0:
                total += self.BIT[i][j]
                j -= j & -j
            i -= i & -i

        return total
    
    def update(self, r, c, val):
        self._update(r, c, val)

    def range_sum(self, top_left, bottom_right):
        r1, c1 = top_left
        r2, c2 = bottom_right

        top_sum = self._sum(r1-1, c2)
        left_sum = self._sum(r2, c1-1)
        top_left_sum = self._sum(r1-1, c1-1)
        bottom_sum = self._sum(r2, c2)

        return bottom_sum - top_sum - left_sum + top_left_sum
    
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

q = QueryMutable(matrix)

print(q.range_sum((0,0), (2,2)))  # 45
print(q.range_sum((1,1), (2,2)))  # 28

q.update(1,1,50)  # change 5 → 50

print(q.range_sum((0,0), (2,2)))  # 90
print(q.range_sum((1,1), (2,2)))  # 73
print(q.range_sum((1,1), (1,1)))  # 50 (single cell)




        
