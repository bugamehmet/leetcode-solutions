class Solution:
    def isPathCrossing(self, path: str) -> bool:
        orj = [0, 0]
        N = [1, 0]
        S = [-1, 0]
        W = [0, 1]
        E = [0, -1]
        
        visited = set()
        visited.add(tuple(orj))
        
        for i in range(len(path)):
            if path[i] == "N":
                orj[0] += N[0]
                orj[1] += N[1]
            elif path[i] == "S":
                orj[0] += S[0]
                orj[1] += S[1]
            elif path[i] == "W":
                orj[0] += W[0]
                orj[1] += W[1]
            else:
                orj[0] += E[0]
                orj[1] += E[1]
            
            current_position = tuple(orj)
            if current_position in visited:
                return True
            
            visited.add(current_position)
        
        return False
