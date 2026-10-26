# 393 — UTF-8 Validation

## Problem
Given an integer array `data` representing the data bytes of a sequence, return `true` if it represents a valid UTF-8 encoding, or `false` otherwise. Each integer in `data` represents 1 byte (only the least significant 8 bits are considered).

A character in UTF-8 can be from 1 to 4 bytes long, subjected to the following rules:
- **1-byte character:** Starts with bit `0` (`0xxxxxxx`).
- **2-byte character:** Starts with `110` (`110xxxxx`), followed by 1 continuation byte (`10xxxxxx`).
- **3-byte character:** Starts with `1110` (`1110xxxx`), followed by 2 continuation bytes (`10xxxxxx`).
- **4-byte character:** Starts with `11110` (`11110xxx`), followed by 3 continuation bytes (`10xxxxxx`).

**Difficulty:** Medium | **Topic:** Bit Manipulation
**[View on LeetCode](https://leetcode.com/problems/utf-8-validation/)**

**Examples:**
```text
Input: data = [197,130,1]
Output: true
Explanation:
- 197 = 11000101 (2-byte header, expects 1 continuation byte)
- 130 = 10000010 (valid continuation byte, begins with 10)
- 1   = 00000001 (valid 1-byte character, begins with 0)
Valid UTF-8 sequence.

Input: data = [235,140,4]
Output: false
Explanation:
- 235 = 11101011 (3-byte header, expects 2 continuation bytes)
- 140 = 10001100 (1st valid continuation byte, begins with 10)
- 4   = 00000100 (2nd byte starts with 0, not a valid continuation byte 10xxxxxx)
Invalid UTF-8 sequence.
```

---

## My Approaches
### Attempt 1 — Bitwise Prefix Checking with Continuation Counter ✅ Final Accepted Solution
**Why I used it:**
Right-shifting each byte isolates its most significant prefix bits. A counter `rem` tracks the expected number of continuation bytes (`10xxxxxx`) remaining for the current multi-byte character.

```python
from typing import List

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
```

**Algorithm Steps:**
1. Initialize a counter `rem = 0` representing the number of continuation bytes expected.
2. Iterate through each integer `num` in `data`:
   - If `rem == 0`, we are looking at the start of a new UTF-8 character:
     - `(num >> 7) == 0`: 1-byte character (`0xxxxxxx`). Valid, continue.
     - `(num >> 5) == 0b110`: 2-byte character header (`110xxxxx`). Set `rem = 1`.
     - `(num >> 4) == 0b1110`: 3-byte character header (`1110xxxx`). Set `rem = 2`.
     - `(num >> 3) == 0b11110`: 4-byte character header (`11110xxx`). Set `rem = 3`.
     - Otherwise, the byte prefix does not match any valid UTF-8 lead byte (e.g., starts with `10` or `11111`), so return `False`.
   - If `rem > 0`, we are expecting a continuation byte:
     - Check if `(num >> 6) == 0b10`. If not, it is not a valid continuation byte (`10xxxxxx`), return `False`.
     - Decrement `rem` by 1.
3. After examining all bytes, return `rem == 0` to confirm no trailing continuation bytes were left unfulfilled.

**Complexity:**
- Time: O(n) — single pass over the array of size `n`, performing constant-time O(1) bitwise operations per byte.
- Space: O(1) auxiliary space — only an integer counter `rem` is maintained.

---

---

## Standard Approach
### Standard Approach 1 — Bitmask Extraction ✅
### Idea
Rather than right-shifting, the standard alternative creates fixed bitmasks (`mask1 = 1 << 7`, `mask2 = 1 << 6`, etc.) to count leading 1-bits until the first 0-bit. If the leading 1s count is 1 or greater than 4, it is invalid; if 0, it is 1-byte; otherwise, `count - 1` continuation bytes are expected. Both approaches share identical asymptotic complexity.

```python
class Solution:
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
```

### Complexity
- Time: O(n) — at most 8 bit checks per byte.
- Space: O(1) auxiliary space.

---

---

## Comparison
| Approach | Time | Space | Recommended |
|-----------|--------|---------|-------------|
| My Approach (Right-Shift Prefix Matching) | O(n) | O(1) | ✅ |
| Standard Approach (Bitmask Leading-1s Count) | O(n) | O(1) | ✅ |

---

## Key Takeaway
Bitwise right-shifting by 7, 5, 4, 3, and 6 cleanly isolates the leading bits of each byte, providing a concise state-machine parser for UTF-8 variable-length encodings with zero memory overhead.

---

## Reference
- LeetCode #393 — UTF-8 Validation
