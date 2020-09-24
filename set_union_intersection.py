#---UNION
even = set(range(0, 40, 2))
print(even)  # {0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38}
print(len(even))  # 20

squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(squares)  # {4, 6, 9, 16, 25}
print(len(squares))  # 5

print(even.union(squares))  # {0, 2, 4, 6, 8, 9, 10, 12, 14, 16, 18, 20, 22, 24, 25, 26, 28, 30, 32, 34, 36, 38}
print(len(even.union(squares)))  # 22 it combines them

print(squares.union(even))


#---INTERSECTION
print("-" * 40)
print(even.intersection(squares)) #{16, 4, 6}
print(even & squares) #{16, 4, 6}
print(squares.intersection(even)) #{16, 4, 6}
print(squares & even) #{16, 4, 6} #only those that are in both sets

#difference_update
print("=" * 40)
print(sorted(even)) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
print(squares) #{4, 6, 9, 16, 25}
even.difference_update(squares)
print(sorted(even)) #[0, 2, 8, 10, 12, 14, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]

#symmetric_difference (all members one set or the other but not in both)
print("=" * 40)
even = set(range(0, 40, 2))
print(sorted(even)) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(sorted(squares)) #[4, 6, 9, 16, 25]

print("symmetric even minus squares")
print(sorted(even.symmetric_difference(squares)))
#[0, 2, 8, 9, 10, 12, 14, 18, 20, 22, 24, 25, 26, 28, 30, 32, 34, 36, 38]

print("symmetric squares minus even")
print(sorted(squares.symmetric_difference(even)))
# [0, 2, 8, 9, 10, 12, 14, 18, 20, 22, 24, 25, 26, 28, 30, 32, 34, 36, 38]

#---discard and remove
print("=" * 40)
even = set(range(0, 40, 2))
print(sorted(even)) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
squares_tuple = (4, 6, 9, 16, 25)
squares = set(squares_tuple)
print(sorted(squares)) #[4, 6, 9, 16, 25]

squares.discard(4)
squares.remove(16)
squares.discard(8)
print(squares) #{6, 9, 25}
try:
    squares.remove(8)
except KeyError:
    print("The item 8 is not a member of the set")


#--subset and superset
print("=" * 40)
even = set(range(0, 40, 2))
print(sorted(even)) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
squares_tuple = (4, 6, 16)
squares = set(squares_tuple)
print(sorted(squares)) #[4, 6, 16]

if squares.issubset(even):
    print("squares is subset of even")
if even.issuperset(squares):
    print("even is a superset of squares")



even = frozenset(range(0, 100, 2))
print(even)
even.add(3)
