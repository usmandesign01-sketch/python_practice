def countdown(n):
    if n == 0:
        print("Blast off!")
        return(n)
    print(n)
    countdown(n-1)

countdown(3)