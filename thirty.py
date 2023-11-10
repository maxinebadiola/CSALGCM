#k = modulo, n = max moves, s = starting num
def solve(k, n, s):

   # all entries are intially "Draw" for all turns (max n)
   dp = [["Draw" for _ in range(k)] for _ in range(n + 1)]
   
   for i in range(n, -1, -1): #loop backwards -> n to 0
      for j in range(k): #all positions (0 -> k-1)
         #if 30, check who's turn, even = alice, odd = bob
         if j == 30: #winner, even = bob, odd = alice
            dp[i][j] = "Bob" if i % 2 == 0 else "Alice"
         #check all possible moves
         elif i < n:
            #adding from 1-3, multiplying from 2-3, squaring
            moves = [(j + x) % k for x in [1, 2, 3]] + [(j * x) % k for x in [2, 3]] + [(j ** 2) % k]
            if i % 2 == 0:
               if any(dp[i + 1][move] == "Alice" for move in moves):
                  dp[i][j] = "Alice"
            else:
               if any(dp[i + 1][move] == "Bob" for move in moves):
                  dp[i][j] = "Bob"

   #return winner
   return dp[0][s]


def main():
    t = int(input())
    ans = []

    for tc in range(t):
        k, n, s = map(int, input().split())
        ans.append(solve(k,n,s))

    print("\n".join(ans))

if __name__ == "__main__":
    main()
