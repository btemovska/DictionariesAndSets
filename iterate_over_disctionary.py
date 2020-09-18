fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}
# while True:
# dict_key = input("Please enter a fruit:")
# if dict_key == "quit":
#     break
# if dict_key in fruit:
#     description = fruit.get(dict_key)
#     print(description)
# else:
#     print("we don't have a " + dict_key)

for snack in fruit:
    print(fruit[snack])

# a sweet, orange, citrus fruit
# good for making cider
# a sour, yellow citrus fruit
# a small, sweet fruit growing in bunches
# a sour, green citrus fruit
print()

for i in range(3):
    for snack in fruit:
        print(snack + " is " + fruit[snack])
    print('-' * 40)
# orange is a sweet, orange, citrus fruit
# apple is good for making cider
#     lemon is a sour, yellow citrus fruit
# grape is a small, sweet fruit growing in bunches
# lime is a sour, green citrus fruit
# ----------------------------------------
# orange is a sweet, orange, citrus fruit
# apple is good for making cider
#     lemon is a sour, yellow citrus fruit
# grape is a small, sweet fruit growing in bunches
# lime is a sour, green citrus fruit
# ----------------------------------------
# orange is a sweet, orange, citrus fruit
# apple is good for making cider
#     lemon is a sour, yellow citrus fruit
# grape is a small, sweet fruit growing in bunches
# lime is a sour, green citrus fruit
# ----------------------------------------
