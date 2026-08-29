def rec(n):
    if n == 0: # base case
        return
    print(n)
    rec(n - 1)
    
rec(5)