fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)
# {'orange': 'a sweet, orange, citrus fruit',
#  'apple': 'good for making cider', 'lemon':
#      'a sour, yellow citrus fruit', 'grape':
#      'a small, sweet fruit growing in bunches',
#  'lime': 'a sour, green citrus fruit'}

print(fruit["lemon"]) #a sour, yellow citrus fruit


#add entry to the dictionary
fruit["pear"] = "an odd shaped apple"
print(fruit)
# {'orange': 'a sweet, orange, citrus fruit',
#  'apple': 'good for making cider',
#  'lemon': 'a sour, yellow citrus fruit',
#  'grape': 'a small, sweet fruit growing in bunches',
#  'lime': 'a sour, green citrus fruit',
#  'pear': 'an odd shaped apple'}


fruit["pear"] = "great with tequila"
print(fruit)  #note this will overwrite the pear entry


#in order to delete an entry
del fruit["lemon"]
#NOTE this deletes the whole fruit variable

#in order to clear all entries but still retail the dictionary
fruit.clear()
# print(fruit) {}