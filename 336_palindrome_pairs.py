# https://leetcode.com/problems/palindrome-pairs/discuss/79209/Accepted-Python-Solution-With-Explanation
# https://leetcode.com/problems/palindrome-pairs/


class Solution:
    
    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]
    
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        words = {word: i for i, word in enumerate(words)}
        valid_pals = []
        for word, k in words.items():
            n = len(word)
            for j in range(n+1):
                pref = word[:j]
                suf = word[j:]
                if self.is_palindrome(pref):
                    back = suf[::-1]
                    if back != word and back in words:
                        valid_pals.append([words[back],  k])
                if j != n and self.is_palindrome(suf):
                    back = pref[::-1]
                    if back != word and back in words:
                        valid_pals.append([k, words[back]])
        return valid_pals
