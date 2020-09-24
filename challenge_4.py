#Create a program that takes some text and returns a list of
#all the characters in the text that are not vowels, sorted in
#alphabetical order.

sampleText = "Python is very powerful language"
vowels = frozenset("aeiou")
finalSet = set(sampleText).difference(vowels)
print(finalSet) #{'l', 'v', 'p', ' ', 'g', 'w', 'n', 'r', 't', 'y', 'P', 'h', 's', 'f'}

finalList = sorted(finalSet)
print(finalList) #[' ', 'P', 'f', 'g', 'h', 'l', 'n', 'p', 'r', 's', 't', 'v', 'w', 'y']



