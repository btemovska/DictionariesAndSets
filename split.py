locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

print(locations[0].split())
# ['You', 'are', 'sitting', 'in', 'front', 'of', 'a', 'computer', 'learning', 'Python']
#split into list containing 10 words
print(locations[3].split(","))
# ['You are inside a building', ' a well house for a small stream']
#it split into a list containing two items, based on the fact we passed
#the parameter of a comma
print(' '.join(locations[0].split()))
# You are sitting in front of a computer learning Python

