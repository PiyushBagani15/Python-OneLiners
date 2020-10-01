def get_permutations(w):
  if len(w)<=1:
    return set(w)
  smaller = get_permutations(w[1:])
  perms = set()
  for x in smaller:
    for pos in range(0,len(x)+1):
      perm = x[:pos] + w[0] + x[pos:]
      perms.add(perm)
  return perms
print(get_permutations("nan"))

# Output
# {'nna', 'ann', 'nan'}
