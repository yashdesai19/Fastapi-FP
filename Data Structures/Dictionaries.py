# create dictionary
tel = {'jack': 4098, 'sape': 4139}
print("Initial dictionary:", tel)

# add new key
tel['guido'] = 4127
print("After adding guido:", tel)

# access value
print("Jack's number:", tel['jack'])

# try to access missing key safely
try:
    print("Value of irv:", tel['irv'])
except KeyError:
    print("Key 'irv' not found (KeyError)")

# safe access using get()
print("Using get('irv'):", tel.get('irv'))

# delete key
del tel['sape']
print("After deleting sape:", tel)

# add irv
tel['irv'] = 4127
print("After adding irv:", tel)

# list of keys
print("Keys as list:", list(tel))

# sorted keys
print("Sorted keys:", sorted(tel))

# membership test
print("Is 'guido' in dictionary?", 'guido' in tel)
print("Is 'jack' NOT in dictionary?", 'jack' not in tel)
