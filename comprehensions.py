squares = []

for i in range(10):
    squares.append(i**2)

print(squares)

squares2 = [i ** 2 for i in range(10)]
print(squares2)

squares3 = [i ** 2 for i in range(30) if i % 3 == 0]
print(squares3)

squares3_dict = {i: i ** 2 for i in range(30) if i % 3 == 0}
print(squares3_dict)


capitals = {'United States':'Washington DC','France':'Paris','Italy':'Rome'}
capitals_by = {capitals[key]: key for key in capitals}
print(capitals_by)




print(sum(i ** 2 for i in range(20)))