
def gen(arr):
    try:
        index = arr.index('?')
    except ValueError:
        print("".join(arr))
        return 

    arr[index] = '0'
    gen(arr.copy())
    
    arr[index] = '1'
    gen(arr.copy())
    
gen(list('??'))
print(list('1?2'))



def gen(s):
    try:
        index = s.index('?')
    except ValueError:
        print(s)
        return 

    s_0 = s[:index] + '0' + s[index+1:]
    gen(s_0)
    
    s_1 = s[:index] + '1' + s[index+1:]
    gen(s_1)
    
gen(list('??'))
print(list('1?2'))