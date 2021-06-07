def qsort (L) : return [] if L == [] else qsort([x for x in L[ 1 :] if x< L[ 0 ]]) + L[ 0 : 1 ] + qsort([x for x in L[ 1 :] if x>=L[ 0 ]])
lst = [ 44 , 33 , 22 , 5 , 77 , 55 , 999 ]
print(qsort(lst))
