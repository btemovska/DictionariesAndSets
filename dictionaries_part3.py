fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

fruit_keys = fruit.keys()
print(fruit_keys) #dict_keys(['orange', 'apple', 'lemon', 'grape', 'lime'])

fruit["tomato"] = "not nice with ice cream"
print(fruit_keys) #dict_keys(['orange', 'apple', 'lemon', 'grape', 'lime', 'tomato'])


print(fruit.items())
# dict_items([('orange', 'a sweet, orange, citrus fruit'),
#             ('apple', 'good for making cider'),
#             ('lemon', 'a sour, yellow citrus fruit'),
#             ('grape', 'a small, sweet fruit growing in bunches'),
#             ('lime', 'a sour, green citrus fruit'),
#             ('tomato', 'not nice with ice cream')])


f_tuple = tuple(fruit.items())
print(f_tuple)
# (('orange', 'a sweet, orange, citrus fruit'),
#  ('apple', 'good for making cider'),
#  ('lemon', 'a sour, yellow citrus fruit'),
#  ('grape', 'a small, sweet fruit growing in bunches'),
#  ('lime', 'a sour, green citrus fruit'),
#  ('tomato', 'not nice with ice cream'))
for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)
# orange is a sweet, orange, citrus fruit
# apple is good for making cider
# lemon is a sour, yellow citrus fruit
# grape is a small, sweet fruit growing in bunches
# lime is a sour, green citrus fruit
# tomato is not nice with ice cream


print(dict(f_tuple))
# {'orange': 'a sweet, orange, citrus fruit',
#  'apple': 'good for making cider',
#  'lemon': 'a sour, yellow citrus fruit',
#  'grape': 'a small, sweet fruit growing in bunches',
#  'lime': 'a sour, green citrus fruit',
#  'tomato': 'not nice with ice cream'}



