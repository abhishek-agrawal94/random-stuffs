import sys
#segmented = "../corpus/segmentedWiki.txt"
#content = open(segmented)
#tokenisedText = "../corpus/tokenised.txt"
#tokenised = open(tokenisedText,'r+')

sent_id = 1
content = sys.stdin.readline()

while content:
    word_id=1
    print("# sent_id = %d"%(sent_id))
    print("# text = %s"%(content))
    #tokenised.write("# sent_id = %d"%(sent_id))
    #tokenised.write("# text = %s"%(content))
    for token in content.split(' '):
        print ("{0} {1} - - - - - - - -".format(word_id,token))
       #tokenised.write("{0} {1} - - - - - - - -".format(word_id,token))
        word_id+=1
    sent_id+=1
    content = sys.stdin.readline()
#tokenised.close()
