# ─────────────────────────────────────────────────
# APPROACH 1: Two Hash Maps (Recommended)
# Time: O(n) | Space: O(1)
# ─────────────────────────────────────────────────
class Solution1:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t, t_to_s = {}, {}
        for cs, ct in zip(s, t):
            if s_to_t.get(cs, ct) != ct or t_to_s.get(ct, cs) != cs:
                return False
            s_to_t[cs] = ct
            t_to_s[ct] = cs
        return True

# ─────────────────────────────────────────────────
# APPROACH 2: Encode Pattern
# Time: O(n) | Space: O(n)
# ─────────────────────────────────────────────────
class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def encode(string):
            mapping = {}
            return [mapping.setdefault(c, len(mapping)) for c in string]
        return encode(s) == encode(t)
