# Given a list of Clock times, merge the overlapping clock times, but there is an edge case where the time wraps, e.g, [23:00, 02:00]. This is 11pm - 2am, 
# the way to handle this is to split it into [23:00, 23:59] and [00:00, 02:00]
# [["22:00", "23:30"], ["23:00", "01:00"], ["00:30", "02:00"]]

# [[2200,2330], [2300, 0100], [0030, 0200]] -> [[2200,2330], [2300, 2359], [0000, 0100], [0030, 0200]]
# [[2200, 2359], [0000,0200]] -> [['00:00', '02:00'], ['22:00', '23:59']]

def convert_interval(interval: list):
    out = [0]*2
    start, end = interval
    
    hour, minu = start.split(':')
    hour1, minu1 = end.split(':')
    
    out[0] = hour + minu
    out[1] = hour1+minu1
    return out
    
def expand_interval(intervals: list):
    out = []
    for interval in intervals:
        start, end = interval
        
        if start > end:
            out.append([start, "2359"])
            out.append(["0000", end])
        else:
            out.append(interval)
    return out
    
def merge_intervals(intervals: list[str]):
    
    converted = []
    
    for interval in intervals:
        converted.append(convert_interval(interval))
        
    expanded = expand_interval(converted)
    expanded.sort()

    solution = [expanded[0]]

    for i in range(1, len(expanded)):
        start, end = expanded[i]
        if int(start) < int(solution[-1][1]):
            solution[-1][1] = max(end, solution[-1][1])
        else:
            solution.append([start, end])

    return solution

def convert_to_time_format(intervals: list[list[str]]):
    ans = []

    for interval in intervals:
        start, end = interval

        start_str = start[:2] + ":" + start[2:]
        end_str = end[:2] + ":" + end[2:]

        ans.append([start_str, end_str])
    return ans

sol = merge_intervals([["22:00", "23:30"], ["23:00", "01:00"], ["00:30", "02:00"]])

print(convert_to_time_format(sol))