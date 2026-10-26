from collections import Counter
from functools import lru_cache

# ─────────────────────────────────────────────────
# MY APPROACH: Memoized DFS with Frequency State Tuple
# Why: Tries distinct characters in sorted order, keeping track of
#      available character counts and whether the prefix already exceeds target.
# Caveat: State space depends on distinct character counts; heavily pruned
#         in practice once greater=True.
# Time: State-space bounded search (pruned DFS)
# Space: O(n) recursion stack + O(S) memoization cache
# ─────────────────────────────────────────────────
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = Counter(s)
        chars = sorted(cnt.keys())
        n = len(s)

        @lru_cache(None)
        def dfs(i, greater, state):
            if i == n:
                return "" if greater else None

            freq = list(state)

            for idx, ch in enumerate(chars):
                if freq[idx] == 0:
                    continue

                if not greater:
                    if ch < target[i]:
                        continue
                    next_greater = ch > target[i]
                else:
                    next_greater = True

                freq[idx] -= 1

                suffix = dfs(i + 1, next_greater, tuple(freq))

                if suffix is not None:
                    return ch + suffix

                freq[idx] += 1

            return None

        initial_state = tuple(cnt[ch] for ch in chars)

        ans = dfs(0, False, initial_state)
        return "" if ans is None else ans


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH: Greedy Pivot Match and Suffix Flush
# Why: Finds the longest prefix that can match target, branches at
#      the rightmost pivot with the smallest valid character > target[pivot],
#      and flushes remaining letters in ascending order.
# Time: O(26 * n) = O(n)
# Space: O(1) auxiliary space (O(26) character count pool)
# ─────────────────────────────────────────────────
class SolutionGreedyPivot:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = Counter(s)
        n = len(s)

        prefix_len = 0
        curr_cnt = Counter(cnt)
        while prefix_len < n and curr_cnt[target[prefix_len]] > 0:
            curr_cnt[target[prefix_len]] -= 1
            prefix_len += 1

        for i in range(prefix_len, -1, -1):
            pool = Counter(cnt)
            for j in range(i):
                pool[target[j]] -= 1

            if i < n:
                candidates = sorted(ch for ch in pool if pool[ch] > 0 and ch > target[i])
                if candidates:
                    chosen = candidates[0]
                    pool[chosen] -= 1
                    suffix = []
                    for ch in sorted(pool.keys()):
                        suffix.append(ch * pool[ch])
                    return target[:i] + chosen + "".join(suffix)

        return ""


# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    sol_greedy = SolutionGreedyPivot()

    # Test 1: Standard permutation greater
    s1, target1 = "abc", "acb"
    expected1 = "bac"
    assert sol.lexGreaterPermutation(s1, target1) == expected1
    assert sol_greedy.lexGreaterPermutation(s1, target1) == expected1
    print("Test 1 passed:", expected1)

    # Test 2: Impossible case
    s2, target2 = "ab", "ba"
    expected2 = ""
    assert sol.lexGreaterPermutation(s2, target2) == expected2
    assert sol_greedy.lexGreaterPermutation(s2, target2) == expected2
    print("Test 2 passed:", expected2)

    # Test 3: Multiple identical characters
    s3, target3 = "aab", "aba"
    expected3 = "baa"
    assert sol.lexGreaterPermutation(s3, target3) == expected3
    assert sol_greedy.lexGreaterPermutation(s3, target3) == expected3
    print("Test 3 passed:", expected3)

    print("All tests passed!")
