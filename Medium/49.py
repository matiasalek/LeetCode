class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = {}        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            if key in res:
                res[key].append(s)
            else:
                res[key] = [s]

        return list(res.values())