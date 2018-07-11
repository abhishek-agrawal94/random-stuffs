

filename = "corpus/wiki.10k.txt"

linecount=0
wordcount=0
charcount=0
for line in open(filename).read():
    if line == "\n":
        linecount+=1
    elif line.isspace():
        wordcount+=1
    elif (line != "\n" and not(line.isspace())):
        charcount+=1
print ("Linecount={0} wordcount={1} charcount={2}".format(linecount,wordcount,charcount))
