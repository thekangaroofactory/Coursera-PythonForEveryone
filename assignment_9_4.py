
# 9.4 Write a program to read through the mbox-short.txt and
# figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address
# to a count of the number of times they appear in the file. After the dictionary is produced,
# the program reads through the dictionary using a maximum loop to find the most prolific committer.

# desired output:
# cwen@iupui.edu 5

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
dic = dict()

for line in fh:
    if line.startswith('From '):
        words = line.split()
        if words[1] not in dic:
            dic[words[1]] = 1
        else:
            dic[words[1]] += 1

main_sender = max(dic, key=dic.get)
print(main_sender, dic[main_sender])


