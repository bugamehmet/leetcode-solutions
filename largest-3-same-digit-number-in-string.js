// Largest 3-Same-Digit Number in String
// substring gruplama yapmak için
// length -2 3'lü son 2 elemanı 3 lü gruplayamayacağı için
var largestGoodInteger = function(num) {
  let list = []

  for(let i = 0; i<=num.length - 2 ; i++){
    let grup = num.substring(i , i+3)
    if(grup[0] == grup[1] && grup[0] == grup[2] && grup[1] == grup[2]){
      list.push(grup)
    }
  }
  if(list.length === 0){
    console.log("");
  } else {
    let maxGrup = list.reduce((max, current)=> max > current ? max : current)
    console.log(maxGrup);
  }
};

largestGoodInteger(6777133339)