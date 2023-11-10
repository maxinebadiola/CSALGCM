def payoutGoal(x, n, g, y, jobs, midpoint):
    totalPayout = 0
    for i in range(n):
        difficulty, payout = jobs[i]
        difficulty, payout = jobs[i]
        # x (skill) > difficulty 
        # x (skill) = difficulty, payout >= y
        # x (skill) < difficulty, payout >= y^2 
        if x + midpoint > difficulty or (x + midpoint == difficulty and payout >= y) or (x + midpoint < difficulty and payout >= y**2):
            totalPayout += payout
    return totalPayout >= g

def solve(x, n, g, y, jobs):
    minSkill = 0 #min skill needed
    maxSkill = 10**9 #max skill 10^9
    result = -1
    jobs.sort(key=lambda job: (-job[1], job[0]))

    while minSkill <= maxSkill:
        midpoint = (minSkill + maxSkill) // 2
        #find minimum skill needed for payout
        if payoutGoal(x, n, g, y, jobs, midpoint):
            result = midpoint
            maxSkill = midpoint - 1
        else:
            minSkill = midpoint + 1

    return result

def main():
    t = int(input())

    ans = []
    for tc in range(t):
        input()
        x, n, g, y = list(map(int, input().split(" ")))

        jobs = [list(map(int, input().split(" "))) for i in range(n)]

        ans.append(solve(x, n, g, y, jobs))

    print("\n".join(list(map(str, ans))))

if __name__ == "__main__":
    main()
