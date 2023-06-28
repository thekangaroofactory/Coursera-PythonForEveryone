
import re

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "regex_sum_1822029.txt"

fh = open(fname)
mylist = list()

for line in fh:
    output = re.findall('[0-9]+', line)
    if output:
        for x in output:
            mylist.append(x)

mylist = [eval(i) for i in mylist]
total = sum(mylist)

print(total)

