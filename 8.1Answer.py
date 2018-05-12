def chop(c):
    del c[len(c)-1]
    del c[0]
numbers = [ '1', '2', '3']
chop(numbers)
print(numbers)
