from typing import List

# ─────────────────────────────────────────────────
# MY APPROACH: Bitwise Prefix Checking with Continuation Counter
# Why: Isolates leading bits using right bitshifts; tracks remaining
#      continuation bytes using a state counter `rem`.
# Time: O(n)
# Space: O(1) auxiliary space
# ─────────────────────────────────────────────────
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        rem = 0
        for num in data:
            if rem == 0:
                if (num >> 7) == 0:
                    continue
                elif (num >> 5) == 0b110:
                    rem = 1
                elif (num >> 4) == 0b1110:
                    rem = 2
                elif (num >> 3) == 0b11110:
                    rem = 3
                else:
                    return False
            else:
                if (num >> 6) != 0b10:
                    return False
                rem -= 1
        return rem == 0


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH: Bitmask Leading-1s Counter
# Why: Uses bitwise masks (1 << 7, etc.) to count leading 1-bits.
# Time: O(n)
# Space: O(1) auxiliary space
# ─────────────────────────────────────────────────
class SolutionMask:
    def validUtf8(self, data: List[int]) -> bool:
        n_bytes = 0

        for num in data:
            bin_rep = num & 0xFF

            if n_bytes == 0:
                mask = 1 << 7
                while mask & bin_rep:
                    n_bytes += 1
                    mask >>= 1

                if n_bytes == 0:
                    continue
                if n_bytes == 1 or n_bytes > 4:
                    return False
                n_bytes -= 1
            else:
                if not (bin_rep & (1 << 7) and not (bin_rep & (1 << 6))):
                    return False
                n_bytes -= 1

        return n_bytes == 0


# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    sol_mask = SolutionMask()

    # Test 1: Valid 1-byte and multi-byte sequence
    valid_data = [197, 130, 1]
    assert sol.validUtf8(valid_data) is True
    assert sol_mask.validUtf8(valid_data) is True
    print("Test 1 (valid) passed:", valid_data)

    # Test 2: Invalid continuation byte
    invalid_data = [235, 140, 4]
    assert sol.validUtf8(invalid_data) is False
    assert sol_mask.validUtf8(invalid_data) is False
    print("Test 2 (invalid) passed:", invalid_data)

    # Test 3: Incomplete multi-byte sequence
    incomplete_data = [235, 140]
    assert sol.validUtf8(incomplete_data) is False
    assert sol_mask.validUtf8(incomplete_data) is False
    print("Test 3 (incomplete) passed:", incomplete_data)

    print("All tests passed!")
