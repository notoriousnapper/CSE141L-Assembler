from bitstring import Bits
import definitions
from definitions import getOp

registers = {
    'r0' : 0,
    'r1' : 1,
    'r2' : 2,
    'r3' : 3,
    'r4' : 4,
    'r5' : 5,
    'r6' : 6,
    'r7' : 7,
    'i0' : 0,
    'i1' : 1,
    'i2' : 2,
    'i3' : 3
}

def addComment():
    theOutputFile.write('    // ')
    for word in words:
        theOutputFile.write(word + ' ')
    theOutputFile.write('\n')

def assembleMachineCode(words, theOutputFile):
    wordCount = len(words)
    if wordCount == 1:
        op = getOp(words[0])
        theOutputFile.write(format(op, 'b').zfill(4))   #b means write in binary
        theOutputFile.write(format(0, 'b').zfill(5))
        addComment()

    if wordCount == 2:
        op = getOp(words[0])
        theOutputFile.write(format(op, 'b').zfill(4))
        if registers.has_key(words[1]):
            register = registers[words[1]]
            theOutputFile.write(format(register, 'b').zfill(3))
            theOutputFile.write(format(0, 'b').zfill(2))
        else:
            immediate = int(words[1])
            if immediate > -1:
                theOutputFile.write(format(immediate, 'b').zfill(5))
            else:
                theOutputFile.write(str(Bits(int = immediate, length = 6).bin))
        addComment()

    if wordCount == 3:
        # If R Type
        op = getOp(words[0])
        reg1 = registers[words[1]]
        reg2 = registers[words[2]]
        theOutputFile.write(format(op, 'b').zfill(4))
        theOutputFile.write(format(reg1, 'b').zfill(3))
        theOutputFile.write(format(reg2, 'b').zfill(2))
        addComment()

    if wordCount == 4: # Shift Op
        # If F Type
        op = getOp(words[0])
        reg1 = registers[words[1]]
        amt = int(words[2])
        direction = int(words[3])


        theOutputFile.write(format(op, 'b').zfill(4))
        theOutputFile.write(format(reg1, 'b').zfill(3))
        theOutputFile.write(format( amt, 'b').zfill(1))
        theOutputFile.write(format( direction, 'b').zfill(1))
        addComment()


if __name__ == "__main__":
    print("Moiz's Stupid Simple Python Assembler:\n")
    print("Beginning Assembly now!")
    with open('SampleAsm.s') as theInputFile, open('machineCode.txt', 'w') as theOutputFile:
        lineCount = 1
        for line in theInputFile:
            print "Assembling line %d" % lineCount
            # print line
            words = line.split()
            # print words
            assembleMachineCode(words, theOutputFile)
            lineCount += 1
