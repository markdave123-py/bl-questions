from collections import defaultdict
#aabbcccc
#aabbccc -> a:2, b:2, c:3 -> 2: 2, 3: 1
def is_cool(s:str):

    counter = defaultdict(int)

    for char in s:
        counter[char] += 1

    counter_vals = defaultdict(int)

    for vals in counter.values():
        counter_vals[vals] += 1

    if len(counter_vals) == 1:
        key, val = counter_vals.items()[0]
        return key == 1 or val == 1
    
    if len(counter_vals) == 2:

        k1, k2 = sorted(counter_vals.keys())

        if k1 == 1 and counter_vals[k1] == 1:
            return True

        # the one of higher frequency occurs once
        if k1 + 1 == k2 and counter_vals[k2] == 1:
            return True
    
    return False

print(is_cool('aabbccc'))
