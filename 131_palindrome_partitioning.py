class Solution:
    
    def __init__(self) -> None:
        """init varz"""
        self._answer = list()
    
    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]
    
    def dfs(self, s: str, path: List[str]) -> None:
        # If we have exhausted `s` to the point where `not s`,
        # then we know we have traversed the graph as far as we
        # can and we are at the last level. Thus, we have traversed
        # from the root to the tail and we append the full path.
        if not s:
            self._answer.append(path)
            return
        
        # If we have not exhausted `s`, look at the prefix and the suffix.
        # If the prefix is a pallindrome, append it to the path and
        # continue traversing on suffix. We do `len(s) + 1` so that we will get
        # a `suffix` value equal to empty string, which is how we denote the end
        # of the graph traversal.
        #
        # We start the range from `1` instead of `0` so that `prefix` is never null.
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            suffix = s[i:]
            if self.is_palindrome(prefix):
                self.dfs(suffix, path + [prefix])
                
    def partition(self, s: str) -> List[List[str]]:
        """Conduct DFS (recursively) until the answer is populated."""
        self.dfs(s, list())
        return self._answer
