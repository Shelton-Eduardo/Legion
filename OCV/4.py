import sys

def maximize_non_adjacent_sum(arr: list[int]) -> int:
    if not arr:
        return 0
        
    # Pythonic space optimization: track only the last two DP states instead of an array
    prev2 = 0  # Represents dp[i-2]
    prev1 = 0  # Represents dp[i-1]
    
    for val in arr:
        # State transition: take current + two steps back, or skip current. Bound at 0.
        current = max(prev1, prev2 + val, 0)
        prev2, prev1 = prev1, current
        
    return prev1

def main():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
        
    # Exclude the first token (N) and parse the rest into integers via comprehension
    arr = [int(x) for x in input_data[1:]]
    
    print(maximize_non_adjacent_sum(arr))

if __name__ == '__main__':
    main()
