var destCity = function(paths) {
  let tum_sehirler = new Set(); // Küme oluşturmak için -- aynı öğeler bulunmaz

  paths.forEach(path => {
      tum_sehirler.add(path[0]);
  });

  for (let i = 0; i < paths.length; i++) {
      let gidilen = paths[i][1];
      if (!tum_sehirler.has(gidilen)) { // tum_sehirler.has(gidilen) gidilen tüm şehirlerde bulunmuyorsa (!) - .has(sahip olmak) --> Metodu belirli nesneye sahip mi kontrolü yapar.
          return gidilen;
      }
  }

  return "";
};

