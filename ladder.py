def my_steps(n):
    def count_ways(n):
        if(n<0):
            return 0
        if(n==0):
            return 1
        if(n<2):
            return n
        
        num = 0
        for i in range(1, 3):
            num+=count_ways(n-i)
        return num
    if n < 1 or n > 25:
        raise ValueError()
    else:
        return count_ways(n)
