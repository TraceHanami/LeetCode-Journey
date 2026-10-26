# ─────────────────────────────────────────────────
# MY APPROACH: Greedy Push-Tier Allocation
# Why: Fill all 8 keys at 1 push, then all 8 at 2 pushes, etc.,
#      minimizing total presses for distinct letters.
# Time: O(len(word))
# Space: O(1) auxiliary space
# ─────────────────────────────────────────────────
class Solution:
    def minimumPushes(self, word: str) -> int:
        cost = {1: 8, 2: 8, 3: 8, 4: 2}
        n = len(word)
        ans = 0
        for pushes, cnt in cost.items():
            take = min(n, cnt)
            ans += take * pushes
            n -= take
            if n == 0:
                break
        return ans


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH: Direct Mathematical Formula
# Why: Compute the sum directly using integer division by 8.
# Time: O(len(word))
# Space: O(1) auxiliary space
# ─────────────────────────────────────────────────
class SolutionMath:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        full_blocks, rem = divmod(n, 8)
        return 4 * full_blocks * (full_blocks + 1) + rem * (full_blocks + 1)


# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    sol_math = SolutionMath()

    # Test 1: word with 5 letters
    assert sol.minimumPushes("abcde") == 5
    assert sol_math.minimumPushes("abcde") == 5
    print("Test 1 ('abcde') passed: 5")

    # Test 2: word with 10 letters
    assert sol.minimumPushes("xycdefghij") == 12
    assert sol_math.minimumPushes("xycdefghij") == 12
    print("Test 2 ('xycdefghij') passed: 12")

    # Test 3: word with 26 letters (all distinct)
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    expected_all = 8 * 1 + 8 * 2 + 8 * 3 + 2 * 4  # 8 + 16 + 24 + 8 = 56
    assert sol.minimumPushes(all_letters) == expected_all
    assert sol_math.minimumPushes(all_letters) == expected_all
    print("Test 3 (26 letters) passed:", expected_all)

    print("All tests passed!")
