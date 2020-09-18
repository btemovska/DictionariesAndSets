fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])

#another example
ordered_keys = list(fruit.keys())
ordered_keys.sort()   #sort
for f in ordered_keys:
    print(f + " - " + fruit[f])
# apple - good for making cider
# grape - a small, sweet fruit growing in bunches
# lemon - a sour, yellow citrus fruit
# lime - a sour, green citrus fruit
# orange - a sweet, orange, citrus fruit
print()

#another example
ordered_keys = sorted(list(fruit.keys()))  #sorted
for f in ordered_keys:
    print(f + " - " + fruit[f])
print()

#another example this is less efficient
for val in fruit.values():
    print(val)
print()

for key in fruit:
    print(fruit[key])


    