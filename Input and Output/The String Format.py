# 1 Basic example
print('We are the {} who say "{}!"'.format('Coders', 'Ni'))

# 2 Position numbers
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

# # 3 Keyword arguments
print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))

# # 4 Mixing positional and keyword
print('The story of {0}, {1}, and {other}.'.format(
      'Bill', 'Manfred', other='Georg'))

# 5 Dictionary with []
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}

print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))

# # 6 Using **
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

# # 7 Using vars()
name = "Yash"
age = 20

table2 = {k: str(v) for k, v in vars().items()}
message = " ".join([f'{k}: ' + '{' + k + '};' for k in table2.keys()])
print(message.format(**table2))

# # 8 Alignment example
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
