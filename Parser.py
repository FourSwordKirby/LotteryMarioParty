#!/usr/bin/env python
import sys

def getWords(filename):
    numbers = [];
    myFile = open(filename);
    for line in myFile :
        for number in line.split(' '):
            number = number.rstrip()
            for number2 in number.split(","):
                number2 = number2.rstrip()
                if number2.isdigit() and len(number2) < 3:
                    numbers.append(number2.rstrip())
    return numbers

def main(dictFile, outputFile):
    numbers = getWords(dictFile)

    #writes everything to output
    newFile = open(outputFile, "w");
    for number in numbers:
        newFile.write(number + " ");
    newFile.close();

#actual command that is run
main(str(sys.argv[1]), str(sys.argv[2]))
#statements used for generating the output and for testing
#main(1, "dictionary.txt", "raw.txt", "outputNorm2.txt")
#main(2, "dictionary.txt", "raw.txt", "outputSwap2.txt")
