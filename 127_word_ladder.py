
# https://leetcode.com/problems/word-ladder/submissions/

from collections import defaultdict, deque
from typing import List, Set

class Solution:
    def __init__(self) -> None:
        """init varz"""
        self._generic_placeholder = "*"
    
    def _compute_generic_states(self, word: str) -> Set[str]:
        res = set()
        for i in range(len(word)):
            # Can't use `str.replace()` here. Blows up for words like `miss` which have a repeating character.
            generic_state = word[:i] + self._generic_placeholder + word[i+1:]
            res.add(generic_state)
        return res
    
    def _build_adj_map(self, wordList: List[str]) -> defaultdict:
        # Pre-processing stage
        # Find all possible generic/intermediate states.
        adj_map = defaultdict(set)
        for word in wordList:
            generic_states = self._compute_generic_states(word)
            for generic in generic_states:
                adj_map[generic].add(word)
        return adj_map
        
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or endWord not in wordList:
            return 0
        
        adj_map = self._build_adj_map(wordList)
        
        # The number represents the level of the node.
        q = deque([(beginWord, 1)])
        visited = set([beginWord])
        while q:
            current_word, current_level = q.popleft()
            all_generic_transformations = self._compute_generic_states(current_word)
            for gt in all_generic_transformations:
                for adj_node_word in adj_map[gt]:
                    if adj_node_word == endWord:
                        return current_level + 1
                    elif adj_node_word not in visited:
                        visited.add(adj_node_word)
                        q.append((adj_node_word, current_level + 1))
        return 0
