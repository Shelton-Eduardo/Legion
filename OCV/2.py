import sys

def minimize_coins_dispensed(target_amount: int, coin_inventory: list[tuple[int, int]]) -> list[tuple[int, int]] | None:
    allocation = []
    remaining = target_amount
    
    for nominal, count in coin_inventory:
        if remaining <= 0:
            allocation.append((nominal, 0))
            continue
            
        actual_take = min(remaining // nominal, count)
        remaining -= actual_take * nominal
        allocation.append((nominal, actual_take))
        
    return allocation if remaining == 0 else None

def main():
    # Read all tokens directly from standard input
    input_tokens = sys.stdin.read().split()
    if not input_tokens:
        return
        
    tokens_iter = iter(input_tokens)
    k = int(next(tokens_iter))
    s = int(next(tokens_iter))
    
    # Collect the coins as a list of (nominal, count) tuples using zip and slicing
    raw_nums = [int(x) for x in tokens_iter]
    coins = list(zip(raw_nums[0::2], raw_nums[1::2]))[:k]
    
    result = minimize_coins_dispensed(s, coins)
    
    if result is not None:
        for nominal, amount_used in result:
            print(f"{nominal}: {amount_used}")
    else:
        print("Impossible")

if __name__ == '__main__':
    main()
