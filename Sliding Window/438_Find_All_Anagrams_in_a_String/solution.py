from typing import *

# ─────────────────────────────────────────────────
# MY APPROACH 1: Fixed-Size Sliding Window with Frequency Maps
# Why: Maintain a frequency map of the current window and compare it to p's frequency map, sliding one character at a time instead of re-counting from scratch.
# Time: O(n)
# Space: O(k) (bounded alphabet)
# ─────────────────────────────────────────────────
class Solution1:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        if len(p) > len(s):
            return result
        need = {}
        for ch in p:
            need[ch] = need.get(ch, 0) + 1
        window = {}
        for i in range(len(p)):
            window[s[i]] = window.get(s[i], 0) + 1
        if need == window:
            result.append(0)
        for i in range(len(p), len(s)):
            left_ch, right_ch = s[i - len(p)], s[i]
            window[left_ch] -= 1
            if window[left_ch] == 0:
                del window[left_ch]
            window[right_ch] = window.get(right_ch, 0) + 1
            if need == window:
                result.append(i - len(p) + 1)
        return result


# ─────────────────────────────────────────────────
# STANDARD / OPTIMAL APPROACH
# Time: O(n)
# Space: O(k)
# ─────────────────────────────────────────────────
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        if len(p) > len(s):
            return []
        need, window = Counter(p), Counter(s[:len(p)])
        result = [0] if need == window else []
        for i in range(len(p), len(s)):
            window[s[i]] += 1
            window[s[i - len(p)]] -= 1
            if window[s[i - len(p)]] == 0:
                del window[s[i - len(p)]]
            if window == need:
                result.append(i - len(p) + 1)
        return result

# ─────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    sol = Solution()
    print("Add test cases here")
