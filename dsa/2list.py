letters = ['a','b','c','d','e','f','g']
print(letters)
# Replace some values
letters[2:5] = ['C','D','E']
print(letters)
#now remove them
letters[2:5] = []
print(letters)
letters[:]=[]
print(letters)
print(len(letters))