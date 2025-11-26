"""

desert = [
    ['.','.','.','o'],
    ['.','.','.','.'],
    ['.','.','.','.'],
    ['.','c','.','.']
]

(desert, 3)

n = len(row)
m = len(cols)

O(nxm) -> 
o(1)

desertWithStation = [
    ['.','.','.','o'],
    ['.','.', '2' ,'.'],
    ['.','.','.','.'],
    ['.','c','.','.']
];

desertWithStationAndRocks = [
    ['.','.','.','o'],
    ['.','r','r','.'],
    ['.','.','r','r'],
    ['c','.','.', 20]
]

"""

from collections import deque

def get_coordinates(desert: list[list[str]]) -> list[tuple[str]]:
    oasis = None
    car = None
    refill = None
    
    for i in range(len(desert)):
        for j in range(len(desert[0])):
            if desert[i][j] == "o":
                oasis = (i, j)
                
            elif desert[i][j] == "c":
                car = (i, j)
                
            elif desert[i][j].isdigit():
                refill = (i, j)
                
                
    return [oasis, car, refill]

def bfs(desert, car, gas):
    direc = ((0,1), (0,-1), (1,0), (-1, 0))
    
    q = deque()
    
    q.append((car[0], car[1], gas))
    
    while q:
        r, c, curgas = q.popleft()
        
        if desert[r][c] == "o":
            return True
            
        for x, y in direc:
            nx, ny = r + x, c + y
            
            if nx < 0 or ny < 0 or nx >= len(desert) or ny >= len(desert[0]) or desert[nx][ny] == 'r':
                continue
            
            new_gas = curgas - 1
            
            if new_gas <= 0:
                continue
                
            q.append((nx, ny, new_gas))
            
    return False
    

    

                

    
    
def can_reach_oasis(desert, gas):
    
    _, car, _ = get_coordinates(desert)
    
    return bfs(desert, car, gas)
    
    # other path
    oasis, car, refill = get_coordinates(desert)
    
    oasis_x, oasis_y = oasis
    
    car_x, car_y = car
    
    refill_x, refill_y = refill
    
    distance_car_oasis = abs(oasis_x - car_x) + abs(oasis_y - car_y)
    
    if distance_car_oasis <= gas:
        return True
        
    distance_car_refill = abs(refill_x - car_x) + abs(refill_y - car_y)
    
    if distance_car_refill > gas:
        return False
        
    distance_refill_oasis = abs(refill_x - oasis_x) + abs(refill_y - oasis_y)
    
    remaining_gas = gas - distance_car_refill
    
    if distance_refill_oasis <= remaining_gas + int(desert[refill_x][refill_y]):
        return True
        
    return False
    
    
    
    