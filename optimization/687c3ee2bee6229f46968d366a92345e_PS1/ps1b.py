###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise
import time
from collections import deque


#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight_dfs(egg_weights, target_weight, memo=None):
    """
    Find the smallest number of eggs that sum up to the target_weight.
    Returns a tuple (count, egg_list).
    count - int, the smallest number of eggs needed
    egg_list - list of the chosen eggs that sum to target_weight
    """
    if memo is None:
        memo = {}

    if target_weight == 0:
        return 0, []
    if target_weight < 0:
        return None, []

    if target_weight in memo:
        return memo[target_weight]

    best_count = None
    best_list = []

    for w in egg_weights:
        count, sub_list = dp_make_weight_dfs(egg_weights, target_weight - w, memo)
        if count is not None:
            candidate = 1 + count
            # Если нашли лучшее решение или оно первое
            if best_count is None or candidate < best_count:
                best_count = candidate
                best_list = [w] + sub_list

    memo[target_weight] = (best_count, best_list)
    return best_count, best_list

def dp_make_weight_bfs(egg_weights, target_weight, memo={}):
    """
    Find the smallest number of eggs that sum up to the target_weight.
    Returns a tuple (count, egg_list).
    count - int, the smallest number of eggs needed
    egg_list - list of the chosen eggs that sum to target_weight
    """
    queue = deque()
    queue.append((0, []))

    sorted_weights = sorted(egg_weights, reverse=True)

    while queue:
        curr_weight, path = queue.popleft()

        if curr_weight == target_weight:
            return len(path), path

        remaining_weight = target_weight - curr_weight

        if remaining_weight in memo:
            full_path = path + memo[remaining_weight][1]
            return len(full_path), full_path


        for w in sorted_weights:

            new_path = path + [w]
            new_weigth = curr_weight + w

            if new_weigth not in memo:
                memo[new_weigth] = (len(new_path), new_path)
                queue.append((new_weigth, new_path))
            else:
                memo[new_weigth] = (len(new_path), new_path) if len(new_path) < len(path) else memo[new_weigth]


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25, 55, 67, 19, 12, 9, 3)
    n = 1000
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    time_dfs = time.time()
    count, res = dp_make_weight_dfs(egg_weights, n)
    dfs_time = time.time() - time_dfs
    print(f"DFS Time: {dfs_time:.6f}")

    time_bfs = time.time()
    count, res = dp_make_weight_bfs(egg_weights, n)
    bfs_time = time.time() - time_bfs
    print(f"BFS Time: {bfs_time:.6f}")
    print("Actual output:", sum(res), count, res)
    print()