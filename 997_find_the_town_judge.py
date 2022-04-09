# https://leetcode.com/problems/find-the-town-judge/

from collections import Counter
from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int: 
        # I personally don't like these edge cases.
        if not trust:
            if n == 1:
                return n
            else:
                return -1
        
        trusters = Counter()
        trustees = Counter()
        all_people = set()
        for truster, trustee in trust:
            all_people.add(truster)
            all_people.add(trustee)
            trusters[truster] += 1
            trustees[trustee] += 1
        
        # Those who trust nobody will be present in all people, but not in the trusters hash map.
        trusts_nobody = all_people.difference(trusters.keys())
        # Those who are trusted by all will be present in the
        # trustees map and have a count equal to n - 1; 
        # the total amount of people in the town minus the judge.
        trusted_by_all = set(k for k, v in trustees.items() if v == n - 1)
        
        if trusts_nobody == trusted_by_all and len(trusts_nobody) == len(trusted_by_all) == 1:
            # Could also be trusted_by_all.pop(). At this point, this is arbitrary.
            return trusts_nobody.pop()
        else:
            return -1
