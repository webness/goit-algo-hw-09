from typing import Dict

coins = [50, 42, 37, 27, 25, 17, 10, 5, 2, 1]


def find_coins_greedy(amount: int) -> Dict[int, int]:
    coin_count = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= count * coin
            coin_count[coin] = count
    return coin_count


def find_min_coins(amount: int) -> Dict[int, int]:
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0  # Base case: 0 coins needed for amount 0

    last_used_coin = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                last_used_coin[i] = coin

    coin_count = {}
    while amount > 0:
        coin = last_used_coin[amount]
        if coin in coin_count:
            coin_count[coin] += 1
        else:
            coin_count[coin] = 1
        amount -= coin

    return coin_count


def compare_algorithms(amount: int):
    import time

    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start_time

    start_time = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start_time

    print(f"Greedy Algorithm Result for {amount}: {greedy_result}, Time: {greedy_time:.6f}s")
    print(f"Dynamic Programming Result for {amount}: {dp_result}, Time: {dp_time:.6f}s")


if __name__ == "__main__":
    amount = 33454
    compare_algorithms(amount)
