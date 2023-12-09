def numberOfMatches(self):
  match_sum = 0
  teams = self.num

  while teams > 1:
      if teams % 2 == 0:
          match_sum += teams // 2
          teams //= 2
      else:
          match_sum += (teams - 1) // 2
          teams = (teams - 1) // 2 + 1