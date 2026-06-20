# ─────────────────────────────────────────────────
# APPROACH 1: Zip and Append (Recommended)
# Time: O(n+m) | Space: O(n+m)
# ─────────────────────────────────────────────────
class Solution1:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for a, b in zip(word1, word2):
            result.append(a)
            result.append(b)
        # Append remainder of longer string
        result.append(word1[len(word2):])
        result.append(word2[len(word1):])
        return ''.join(result)

# ─────────────────────────────────────────────────
# APPROACH 2: Single Index Loop
# Time: O(n+m) | Space: O(n+m)
# ─────────────────────────────────────────────────
class Solution2:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
        return ''.join(result)
