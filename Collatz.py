

memo = {1:0}
def collatz(n:int):

    if n in memo:
        return memo[n]
    
    if n % 2 == 0:
        val = 1 + collatz(n//2)
        memo[n] = val
        return val
    
    else:
        val = 1 + collatz(3*n+1)
        memo[n] = val
        return val
    

print(collatz(3))
