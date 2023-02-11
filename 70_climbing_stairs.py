# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?

def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2
    elif n > 2:
        var = [0] * (n+1)
        #var[0] = 0
        var[1] = 1
        var[2] = 2
        for i in range(3,n+1):
            var[i] = var[i-1] + var[i-2]
        return var[n]
        #return (climbStairs(n-1) + climbStairs(n-2))



def main() :
    n = 39
    print(climbStairs(n))


if __name__ == '__main__':
    main()
