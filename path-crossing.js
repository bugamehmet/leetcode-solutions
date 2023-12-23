var isPathCrossing = function(path) {
  let orj = [0, 0];
  let N = [1, 0];
  let S = [-1, 0];
  let W = [0, 1];
  let E = [0, -1];

  let visited = new Set();
  visited.add(orj.toString());

  for (let i = 0; i < path.length; i++) {
      if (path[i] === "N") {
          orj[0] += N[0];
          orj[1] += N[1];
      } else if (path[i] === "S") {
          orj[0] += S[0];
          orj[1] += S[1];
      } else if (path[i] === "W") {
          orj[0] += W[0];
          orj[1] += W[1];
      } else {
          orj[0] += E[0];
          orj[1] += E[1];
      }

      let current_position = orj.toString();
      if (visited.has(current_position)) {
          return true;
      }

      visited.add(current_position);
  }

  return false;
}