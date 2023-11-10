import bisect
"""
This function solves a test case.

Parameters:
k : int - number of transmission frequencies
n : int - number of participants
fs : array-like - array of size (k,) with a list of transmission frequencies
ms : array-like - array of size (n,) with a list of participant frequencies

Returns a list of integers of size (n,) indicating the answers for each 
participant
"""
def solve(k,n,fs,ms):
    # compute and return answers here
    fs.sort() #sort list 
    participantAnswers = []
    
    for i in range(n):
        frequencyHeard = bisect.bisect_right(fs,ms[i])
        participantAnswers.append(frequencyHeard)
        
    return participantAnswers
    

def main():
    k,n = list(map(int,input().split(" ")))

    fs = sorted([int(input()) for i in range(k)])
    ms = [int(input()) for i in range(n)]

    ans = solve(k,n,fs,ms)

    print("\n".join(list(map(str,ans))))

if __name__ == "__main__":
    main()
