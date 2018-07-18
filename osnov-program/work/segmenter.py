import sys
#corpus = "../corpus/wiki.10k.txt"
#count = 0
#content = open(corpus)
#segmentedText = "../corpus/segmentedWiki.txt"
#segmented = open(segmentedText,'r+')
line = sys.stdin.readline()
while line:
    if ". " in line:
        #count+=1
        line = line.replace(". ",".\n")
    #segmented.write(line)
    print(line)
    line = sys.stdin.readline()
#segmented.close()
#print(count)

