"""
List is a compound data type of python
"""
squares = [1, 4, 9, 16, 25, 27, 28, 29, 30, 33, 12,
           2, 1, 4, 6, 8, 2, 3, 1, 6, 8, 4, 5, 3, 2, 3]
print(len(squares))
print(squares[2:len(squares)-4])
# # List can be indexed and sliced
# print(squares[0])
# print(squares[-1])
# print(squares[-3:]) # slicing returns a new list
# # Lists also support operations like concatenation:
# print(squares + [36, 49, 64, 81, 100])
# # lists are a mutable type, i.e. it is possible to change their content:
# cubes = [1, 8, 27, 65, 125] # something's went wrong here
# print(cubes)
# cubes[3] = 4**3 # replace the wrong value
# print(cubes)
# # can also add new items at the end of the list, by using the append() method
# cubes.append(216)
# cubes.append(7 ** 3) # and add the cube of 7
# print(cubes)
