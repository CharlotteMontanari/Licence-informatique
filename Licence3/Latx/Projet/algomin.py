def Min(L) -> int:
   i = 2
   min = L[i]
   while i <= len(L):
      if L[i] < min:
         min = L[i]
      i += 1
   return min