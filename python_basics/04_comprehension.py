squares = [x * x for x in range(1, 21)]
print(squares)

even_squares = [x * x for x in range(1, 21) if x % 2 == 0]
print(even_squares)

upper = [w.upper() for w in ["apple", "banana", "kiwi"]]
print(upper)

square_map = {x: x * x for x in range(1, 6)}
print(square_map)
