# https://leetcode.com/problems/reconstruct-itinerary/

from typing import List
from collections import defaultdict


class Solution:

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        adj_list = defaultdict(list)
        for f, t in tickets:
            adj_list[f].append(t)
            # Inserts the key but leaves an empty list.
            adj_list[t]
        
        result = list()
        def _dfs(city: str) -> None:
            while adj_list[city]:
                next_stop = adj_list[city].pop()
                _dfs(next_stop)
            result.append(city)
        
        _dfs("JFK")
        return list(reversed(result))
