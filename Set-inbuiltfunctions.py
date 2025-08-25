#Set inbuilt functions

#add

# set1={25,6,15}
# set1.add(8)
# print(set1)           # {25,6,15,8}

# #remove

# set1={2,9,8}
# set1.remove(15)
# print(set1)           # {2,9}

# # discard

# set1={4,5,6}
# set1.discard(15)
# print(set1)           # {4,5}

# #pop

# set1={2,4,6,8}
# set1.pop()            # Removes and returns a random element
# print(set1)

#clear

# set1={3,6,9,5}
# set1.clear()
# print(set1)             # Removes all elements

#copy

# set1={25,6,18}
# c=set1.copy()
# print(c)                 #{25,6,18}

#frozensets

#Union

# fset1=frozenset([25,6,18,15])
# fset2=frozenset([18,15,4,2])
# print(fset1.union(fset2))               # frozenset({2,4,6,15,18,25})

#Intersection

# fset1=frozenset([25,6,18,15])
# fset2=frozenset([18,15,4,2])
# print(fset1.intersection(fset2))           # frozenset({18,15})

#difference

# fset1=frozenset([25,6,18,15])
# fset2=frozenset([18,15,4,2])
# print(fset1.difference(fset2))             # frozenset({25,6})

#symmetric_difference

# fset1=frozenset([25,6,18,15])
# fset2=frozenset([18,15,4,2])
# print(fset1.symmetric_difference(fset2))        #frozenset({2,4,6,25})

#issubset

# fset1=frozenset([25,6,18,15])
# fset2=frozenset([18,15,4,2])
# print(fset1.issubset(fset2))                      # False

#issuperset

# fset1=frozenset([25,6,18,15])
# fset2=frozenset([18,15,4,2])
# print(fset1.issuperset(fset2))                    #False

#isdisjoint

# fset1=frozenset([25,6,18,15])
# fset2=frozenset([18,15,4,2])
# print(fset1.isdisjoint(fset2))                     #False

# Since frozenset is immutable, methods that modify the set are NOT allowed

# fset1=frozenset([25,6,18,15])
# fset1.add()                                        # AttributeError
# fset1.remove()                                     # AttributeError
# fset1.discard()                                    # AttributeError
# fset1.pop()                                        # AttributeError
# fset1.clear()                                      # AttributeError
# fset1.update([])                                   # AttributeError

