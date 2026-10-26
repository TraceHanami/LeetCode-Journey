from typing import List

# ─────────────────────────────────────────────────
# MY APPROACH: Sort by Start and Greedy Merge
# Why: Sorting by start time groups overlapping intervals
#      consecutively; a single linear scan merges adjacent overlaps.
# Note: Assumes input `intervals` is non-empty (guaranteed by constraints).
# Time: O(n log n)
# Space: O(n) (merged list + Timsort scratch space)
# ─────────────────────────────────────────────────
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        m = [intervals[0]]
        for i in intervals[1:]:
            if m[-1][1] >= i[0]:
                m[-1][1] = max(m[-1][1], i[1])
            else:
                m.append(i)
        return m


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH: Sort with Empty Guard
# Why: Same greedy merge strategy, including an explicit check for empty inputs.
# Time: O(n log n)
# Space: O(n)
# ─────────────────────────────────────────────────
class SolutionStandard:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for current in intervals[1:]:
            prev = merged[-1]
            if prev[1] >= current[0]:
                prev[1] = max(prev[1], current[1])
            else:
                merged.append(current)

        return merged


# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    sol_std = SolutionStandard()

    # Test 1: Overlapping intervals
    input_1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    expected_1 = [[1, 6], [8, 10], [15, 18]]
    assert sol.merge([list(x) for x in input_1]) == expected_1
    assert sol_std.merge([list(x) for x in input_1]) == expected_1
    print("Test 1 passed:", expected_1)

    # Test 2: Adjacent touching intervals
    input_2 = [[1, 4], [4, 5]]
    expected_2 = [[1, 5]]
    assert sol.merge([list(x) for x in input_2]) == expected_2
    assert sol_std.merge([list(x) for x in input_2]) == expected_2
    print("Test 2 passed:", expected_2)

    # Test 3: Completely contained intervals
    input_3 = [[1, 4], [2, 3]]
    expected_3 = [[1, 4]]
    assert sol.merge([list(x) for x in input_3]) == expected_3
    assert sol_std.merge([list(x) for x in input_3]) == expected_3
    print("Test 3 passed:", expected_3)

    print("All tests passed!")
