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



