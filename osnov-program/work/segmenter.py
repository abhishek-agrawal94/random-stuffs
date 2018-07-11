corpus = "../corpus/wiki.10k.txt"
count = 0
content = open(corpus)
segmentedText = "../corpus/segmentedWiki.txt"
segmented = open(segmentedText,'r+')

for line in content:
    if ". " in line:
        count+=1
        line = line.replace(". ",".\n")
    segmented.write(line)
segmented.close()
print(count)

