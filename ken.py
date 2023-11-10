MOD = 1000000007

def main():
    # compute a fill DP table here
    dp = [0] * 300000 #max = 3 x 10^5
    
    dp[0] = 1 #base case P(0) = 1
    
    #formula to dismantle patriachy 
    # 3 * P(n-1) + 2 * P(n/2)
    for i in range (1, 300000):
        #user integer divison + mod
        dp[i] = (3*dp[i-1] + 2*dp[i//2]) % MOD 
    
    # no need to touch these lines
    t = int(input())
    ans = []
    for tc in range(t):
        n = int(input())
        ans.append(dp[n])
    print("\n".join(list(map(str,ans))))

if __name__ == "__main__":
    main()
