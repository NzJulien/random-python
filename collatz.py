"""Collatz conjecture explorer: finds the starting number under a limit with the longest chain."""
import sys


def collatz_length(n: int, cache: dict[int, int]) -> int:
    path = []
    while n not in cache:
        path.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    length = cache[n]
    for value in reversed(path):
        length += 1
        cache[value] = length
    return length


def longest_chain(limit: int) -> tuple[int, int]:
    cache = {1: 1}
    best = max(range(1, limit), key=lambda n: collatz_length(n, cache))
    return best, cache[best]


if __name__ == "__main__":
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 1_000_000
    start, length = longest_chain(limit)
    print(f"Under {limit:,}, {start:,} has the longest Collatz chain: {length} steps.")
