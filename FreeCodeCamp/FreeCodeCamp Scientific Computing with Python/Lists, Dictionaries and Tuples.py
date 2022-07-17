# Reading each line at a time
fhandle = open('C:\\Users\\lucaa\\Desktop\\GitHub\\deep-learning-roadmap\\FreeCodeCamp Scientific Computing with Pytohn\\mbox-short.txt', 'r')

for line in fhandle:
    sentence = line.strip()
    print(sentence)


# Reading the whole file
input_file = fhandle.read()
print(input_file[:20])

# Search through the file
fhandle = open('C:\\Users\\lucaa\\Desktop\\GitHub\\deep-learning-roadmap\\FreeCodeCamp Scientific Computing with Pytohn\\mbox-short.txt', 'r')
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)


# Working with lists
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# Building a list from scratch
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

# Checking if an element is inside a list
'cookie' in stuff

# Sorting a list
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends) 

# Get the average of a list of numbers provided by the user
numbers = list()
while True:
    input_number = input('Enter a number: ')
    if input_number == 'done':
        break
    else:
        numbers.append(float(input_number))


print('The average of the numbers is: ' + sum(numbers)/len(numbers))


# Strings and lists
abc = 'With three words'
stuff = abc.split()
print(stuff)

for word in stuff:
    print(word)


# Splitting with delimiters
line = 'a; lot; of; words'
etc = line.split()
print(etc)

words = line.split(';')
print(words)

# Working with a file
fhandle = open('C:\\Users\\lucaa\\Desktop\\GitHub\\deep-learning-roadmap\\FreeCodeCamp Scientific Computing with Pytohn\\mbox-short.txt', 'r')
for line in fhandle:
    line = line.rstrip()
    if line.startswith('From:'):
        words = line.split()

print(words)

# Working with dictionaries
d = dict()
d = {'Mon': 31, 'Wed': 4, 'Sat': 15}
print(d['Mon'])

d['Mon'] = 12
print(d)

# Making a histogram with a dictionary
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name in counts:
        counts[name] = counts[name] + 1
    else:
        counts[name] = 1

print(counts)

# Using the get method
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1

print(counts)


## Dictionaries and loops

# Counting words in a line of text
counts = dict()
text = 'the quick brown fox jumps over the lazy dog'
words = text.split()

for word in words:
    counts[word] = counts.get(word,0) + 1

print(counts)

# print the number of unique words in the text
print(len(counts))

# Looping through the keys and values of a dictionary
counts = {'chuck': 1, 'annie': 42, 'jan': 100}

for key in counts:
    print(key, counts[key])


print(list(counts)) # Converting to keys takes only the keys of a dictionary
print(counts.keys()) # Using the .keys method takes only the keys of a dictionary
print(counts.values()) # Using the .values method takes only the values of a dictionary
print(counts.items()) # Using the .items method takes both the keys and values of a dictionary


fhandle = open('C:\\Users\\lucaa\\Desktop\\GitHub\\deep-learning-roadmap\\FreeCodeCamp Scientific Computing with Pytohn\\mbox-short.txt', 'r')
counts = dict()

for line in fhandle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

frequent_word = None
frequent_word_count = None

for word,count in counts.items():
    if frequent_word is None or counts[word] > counts[frequent_word]:
        frequent_word = word
        frequent_word_count = counts[word]

print(frequent_word, frequent_word_count)


# Exercise
counts = {'chuck': 1, 'annie': 42, 'jan': 100}
for key in counts:
    if counts[key]>10:
        print(key, counts[key])


# Working with tuples

# Sorting a dictionary
d = {'c': 4, 'd': 3, 'b': 2, 'a': 1}
print(sorted(d.items()))

# Sorting by values
d = {'c': 3, 'd': 2, 'b': 2, 'a': 5}
print(sorted(d.items(), key=lambda kv: kv[1]))

# Print out the 10 most common words in the text
fhandle = open('C:\\Users\\lucaa\\Desktop\\GitHub\\deep-learning-roadmap\\FreeCodeCamp Scientific Computing with Pytohn\\mbox-short.txt', 'r')
counts = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1


lst = list()
for key, value in counts.items():
    lst.append((value, key))

lst = sorted(lst, reverse=True)

for value, key in lst[:10]:
    print(key, value)

# Short version
common_words = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
for word, count in common_words[:10]:
    print(word, count)

print(common_words[:10])


