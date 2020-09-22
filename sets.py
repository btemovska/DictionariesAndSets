farm_animals = {"sheep", "cow","hen"}
print(farm_animals) #{'hen', 'sheep', 'cow'}

for animal in farm_animals:
    print(animal)
# hen
# sheep
# cow

print("=" * 40)

wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
print(wild_animals) #{'elephant', 'hare', 'lion', 'tiger', 'panter'}
for animal in wild_animals:
    print(animal)
# elephant
# hare
# lion
# tiger
# panther

farm_animals.add("horse")
wild_animals.add("horse")

print(farm_animals) #{'hen', 'cow', 'horse', 'sheep'}
print(wild_animals) #{'lion', 'elephant', 'hare', 'horse', 'tiger', 'panther'}

