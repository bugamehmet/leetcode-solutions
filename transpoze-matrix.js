var transpose = function(matrix) {
  let result = [];
  for(let i = 0; i < matrix[0].length; i++){
      let column = [];
      for(let j = 0; j < matrix.length; j++){
          column.push(matrix[j][i]);
      };
      result.push(column);
  };
  return result
};