class Point:
    def __init__(self, a: int, b: int):
        self.x = a
        self.y = b


class Solution:
    def countShips(self, sea, topRight, bottomLeft):
        x1, y1 = bottomLeft.x, bottomLeft.y
        x2, y2 = topRight.x,   topRight.y

        # invalid rectangle
        if x1 > x2 or y1 > y2:
            return 0

        # if no ships in this rectangle, prune immediately
        if not sea.hasShips(topRight, bottomLeft):
            return 0

        # if reduced to a single point and hasShips is true => 1 ship
        if x1 == x2 and y1 == y2:
            return 1

        # split the rectangle into 4
        mx = (x1 + x2) // 2
        my = (y1 + y2) // 2

        total = 0

        # top-left
        total += self.countShips(sea,
                                 Point(mx, y2),
                                 Point(x1, my + 1))

        # top-right
        total += self.countShips(sea,
                                 Point(x2, y2),
                                 Point(mx + 1, my + 1))

        # bottom-left
        total += self.countShips(sea,
                                 Point(mx, my),
                                 Point(x1, y1))

        # bottom-right
        total += self.countShips(sea,
                                 Point(x2, my),
                                 Point(mx + 1, y1))

        return total


# | Quadrant     | bottomLeft   | topRight |
# | ------------ | ------------ | -------- |
# | Top-Left     | (x1, my+1)   | (mx, y2) |
# | Top-Right    | (mx+1, my+1) | (x2, y2) |
# | Bottom-Left  | (x1, y1)     | (mx, my) |
# | Bottom-Right | (mx+1, y1)   | (x2, my) |

# # TOP LEFT
# count += countShips(sea,
#                     topRight   = (mx,  y2),
#                     bottomLeft = (x1,  my+1))

# # TOP RIGHT
# count += countShips(sea,
#                     topRight   = (x2,  y2),
#                     bottomLeft = (mx+1, my+1))

# # BOTTOM LEFT
# count += countShips(sea,
#                     topRight   = (mx,  my),
#                     bottomLeft = (x1,  y1))

# # BOTTOM RIGHT
# count += countShips(sea,
#                     topRight   = (x2,  my),
#                     bottomLeft = (mx+1, y1))
