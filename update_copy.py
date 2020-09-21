fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)
veg = {"cabbage": "every child's favorite",
       "sprouts": "mmmm, loveley",
       "spinach": "can I have more fruit, please"}
print(veg)

veg.update(fruit)  #it adds the two dictionaries together
print(veg)
# {'cabbage': "every child's favorite",
#  'sprouts': 'mmmm, loveley',
#  'spinach': 'can I have more fruit, please',
#  'orange': 'a sweet, orange, citrus fruit',
#  'apple': 'good for making cider',
#  'lemon': 'a sour, yellow citrus fruit',
#  'grape': 'a small, sweet fruit growing in bunches',
#  'lime': 'a sour, green citrus fruit'}
print()


#creating a new dictionary by coping the older ones
nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty) #it also combined them

