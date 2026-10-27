```python
# ─────────────────────────────────────────────────
# MY APPROACH: Iterative Base-26 Conversion
# Why: Subtract 1 to handle 1-based Excel numbering,
#      then extract letters using modulo and division.
# Time: O(log_26 n)
# Space: O(log_26 n)
# ─────────────────────────────────────────────────
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ""

        while columnNumber > 0:
            columnNumber -= 1
            r = columnNumber % 26
            s = chr(r + ord('A')) + s
            columnNumber //= 26

        return s


# ─────────────────────────────────────────────────
# STANDARD APPROACH: Base-26 Conversion with a List
# Why: Append letters as they are generated, then
#      reverse and join them to form the title.
# Time: O(log_26 n)
# Space: O(log_26 n)
# ─────────────────────────────────────────────────
class SolutionStandard:
    def convertToTitle(self, columnNumber: int) -> str:
        a = []

        while columnNumber > 0:
            columnNumber -= 1
            r = columnNumber % 26
            a.append(chr(r + ord('A')))
            columnNumber //= 26

        return "".join(a[::-1])


# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    std = SolutionStandard()

    # Test 1: columnNumber = 1
    exp = "A"
    assert sol.convertToTitle(1) == exp
    assert std.convertToTitle(1) == exp
    print("Test 1 passed:", sol.convertToTitle(1))

    # Test 2: columnNumber = 28
    exp = "AB"
    assert sol.convertToTitle(28) == exp
    assert std.convertToTitle(28) == exp
    print("Test 2 passed:", sol.convertToTitle(28))

    # Test 3: columnNumber = 701
    exp = "ZY"
    assert sol.convertToTitle(701) == exp
    assert std.convertToTitle(701) == exp
    print("Test 3 passed:", sol.convertToTitle(701))

    # Test 4: columnNumber = 52
    exp = "AZ"
    assert sol.convertToTitle(52) == exp
    assert std.convertToTitle(52) == exp
    print("Test 4 passed:", sol.convertToTitle(52))

    # Test 5: columnNumber = 2147483647
    assert sol.convertToTitle(2147483647) == std.convertToTitle(2147483647)
    print("Test 5 passed: Maximum constraint")

    print("All tests passed!")
```
