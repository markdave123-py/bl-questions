from collections import deque

def get_coordinates(arr):
    oasis = None
    car = None
    refill = None

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == "o":
                oasis = (i,j)

            elif arr[i][j] == 'c':
                car = (i,j)

            elif arr[i][j].isdigit():
                refill = (i, j)

    return [oasis, car, refill]

    


def can_reach(arr, gas):

    oasis, car, refill = get_coordinates(arr=arr)

    oasis_x, oasis_y = oasis
    car_x, car_y = car
    refill_x, refill_y = refill

    distance_car_oasis = abs(car_x-oasis_x) + abs(car_y-oasis_y)

    distance_car_refill = abs(car_x-refill_x) + abs(car_y-refill_y)

    distance_refill_oasis = abs(oasis_x-refill_x) + abs(oasis_y-refill_y)

    if distance_car_oasis <= gas:
        return True
    
    if distance_car_refill > gas:
        return False
    
    remaining_gas = gas - distance_car_refill
    
    if distance_refill_oasis <= int(arr[refill_x][refill_y]) + remaining_gas:
        return True
    
    return False






def reach_oasis(arr, gas):
    direc = ((0,-1), (-1,0), (0,1), (1,0))
    best_gas = {}
    
    def bfs(sr, sc, gas):
        q = deque()
        q.append((sr, sc, gas))
        best_gas[(sr, sc)] = gas
            
        while q:
            # for _ in range(len(q)):
            r, c, curgas = q.popleft()

            
            if arr[r][c] == "o":
                return True
                
            for x, y in direc:
                nx, ny = r+x, c+y
                if nx < 0 or nx >= len(arr) or ny < 0 or ny >= len(arr[0]) or arr[nx][ny] == 'r':
                    continue

                ngas = curgas - 1
                if ngas < 0:
                    continue
                if arr[nx][ny].isdigit():
                    ngas += int(arr[nx][ny])

                if ngas > best_gas.get((nx, ny), -1):
                    best_gas[(nx,ny)] = ngas
                    q.append((nx, ny, ngas))   
        return False

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'c':
                return bfs(i, j, gas)
        
ans = reach_oasis([['.', '.', '.', 'c', '.'],['.', '.', '.', 'r', '.'],['.', '.', '.', '.', '.'],[ '.', '.', 'o', '.', '.']], 4)
print(ans)