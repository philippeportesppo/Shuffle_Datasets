import random
import sys
import csv

with open(sys.argv[2]+"_learn.tsv", mode='w') as fd:
    writer = csv.writer(fd, delimiter='\t', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["id",	"sentiment",	"review"])
fd.close
    
with open(sys.argv[2]+"_valid.tsv", mode='w') as fd:
    writer = csv.writer(fd, delimiter='\t', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["id",	"sentiment",	"review"])
fd.close

with open(sys.argv[2]+"_test.tsv", mode='w') as fd:
    writer = csv.writer(fd, delimiter='\t', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["id",	"review"])
fd.close

remainingLines=0

with open(sys.argv[1], mode='r')as fd_read:
    reader = csv.reader(fd_read, delimiter='\t', lineterminator='\n')
    numlines = sum(1 for row in reader)
    
    print "Found: "+str(numlines)+" lines in "+sys.argv[1]
     
    remainingLines=int(float(numlines)*0.60)
    print "Shuffle..."
    
    fd_shuffle=open(sys.argv[2]+"_shuffle.tsv", mode='w')
    fd_read.seek(0)
    lines = fd_read.readlines()
    random.shuffle(lines)
    fd_shuffle.writelines(lines)
    fd_shuffle.close
fd_read.close

with open(sys.argv[2]+"_shuffle.tsv", mode='r')as fd_read:
    reader = csv.reader(fd_read, delimiter='\t', lineterminator='\n', quoting=csv.QUOTE_NONNUMERIC)

    print "Split into "+str(remainingLines)+" samples for "+sys.argv[2]+"_learn.tsv"
    print "and "+str(numlines-remainingLines)+" samples for "+sys.argv[2]+"_test.tsv" 
    
    with open(sys.argv[2]+"_learn.tsv", mode='a') as fd_learn:
        print "---"
        with open(sys.argv[2]+"_valid.tsv", mode='a') as fd_valid:
            print "----"
            with open(sys.argv[2]+"_test.tsv", mode='a') as fd_test:
                print "-----"
                
                writer_learn = csv.writer(fd_learn, delimiter='\t', lineterminator='\n', quoting=csv.QUOTE_NONNUMERIC)
                writer_test = csv.writer(fd_test, delimiter='\t', lineterminator='\n', quoting=csv.QUOTE_NONNUMERIC)
                writer_valid = csv.writer(fd_valid, delimiter='\t', lineterminator='\n', quoting=csv.QUOTE_NONNUMERIC)
                print "------"
                currentLine=1
                print "-------"

                for row in reader:
                    #print '',
                    if currentLine<remainingLines:
                        #print ".",
                        writer_learn.writerow([int(row[0]), int(row[2]), row[3]])
                    else:
                        #print "#",
                        writer_valid.writerow([int(row[0]), int(row[2]), row[3]])
                        writer_test.writerow([int(row[0]),  row[3]])
                    currentLine=currentLine+1

