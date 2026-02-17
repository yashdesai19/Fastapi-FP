# create set with duplicates
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print("Basket (duplicates removed):", basket)

# membership testing
print("Is 'orange' in basket?", 'orange' in basket)
print("Is 'crabgrass' in basket?", 'crabgrass' in basket)

# create sets from words
a = set('abracadabra')
b = set('alacazam')

print("\nSet a (unique letters):", a)
print("Set b (unique letters):", b)

# set operations
print("\nLetters in a but not in b (a - b):", a - b)
print("Letters in a or b or both (a | b):", a | b)
print("Letters in both a and b (a & b):", a & b)
print("Letters in a or b but not both (a ^ b):", a ^ b)
