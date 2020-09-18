fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
while True:
    dict_key = input("Please enter a fruit:")
    if dict_key == "quit":
        break
    description = fruit.get(dict_key, "We don't have a " + dict_key)
    print(description)

# Please enter a fruit:apple
# good for making cider
# Please enter a fruit:lemon
# a sour, yellow citrus fruit
# Please enter a fruit:peach
# We don't have a peach
# Please enter a fruit:


