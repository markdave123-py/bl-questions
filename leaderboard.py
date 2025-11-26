import heapq

class TopPlayers:
    def __init__(self, n):
        self.n = n
        self.map = {}
        self.heap = []
    
    def add_player(self, name, score):
        version = 1
        if name in self.map:
            _, ver = self.map[name]
            version += ver
        self.map[name] = (score, version)
        heapq.heappush(self.heap, (-score, version, name))

    def get_top_n(self):
        k = self.n
        out = []
        temp = []
        while self.heap and k > 0:
            score, version, name = heapq.heappop(self.heap)
            if version != self.map[name][1]:
                continue
            out.append((name, -score))
            temp.append((score, version, name))
            k-= 1

        for val in temp:
            heapq.heappush(self.heap, val)

        return out
    

tp = TopPlayers(2)

tp.add_player("d", 3)
tp.add_player("v", 5)
tp.add_player("c", 1)
tp.add_player("d", 0)

print(tp.get_top_n())