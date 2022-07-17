# Working with regular expressions
import re

fhandle = open('C:\\Users\\lucaa\\Desktop\\GitHub\\deep-learning-roadmap\\FreeCodeCamp Scientific Computing with Pytohn\\mbox-short.txt', 'r')
for line in fhandle:
    line = line.rstrip()
    if re.search('From:', line):
        words = line.split()
        print(words)


# Matching and extracting data
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)


s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting at 2pm'
lst = re.findall('\S+@\S+', s)
print(lst)

# Practical applications of regular expressions
# Extracting all the email addresses from a text file
fhandle = open('C:\\Users\\lucaa\\Desktop\\GitHub\\deep-learning-roadmap\\FreeCodeCamp Scientific Computing with Pytohn\\mbox-short.txt', 'r')
for line in fhandle:
    line = line.rstrip()
    email = re.findall('\S+@\S+', line)
    if len(email) > 0:
        print(email)
