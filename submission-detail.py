from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_map = defaultdict(int)
        
        for num in arr:
            count_map[num] += 1
        
        occurrence_set = set()
    
        for count in count_map.values():
            if count in occurrence_set:
                return False
            occurrence_set.add(count) 
            
        return True
