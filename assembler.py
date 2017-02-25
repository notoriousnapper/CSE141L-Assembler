# PART I: ASSEMBLER  ##################################################
# THREE STEPS
# 1. Implement a counter that keeps track of what line an instruction is on
# 2. Write the case for branching that uses relative branching to jump negative or positive
# movements forward
#     - Make sure:
#         1. numbers are signed, given 5 bits for the immediate value for branching
#                 _ _ _ _ | _ _ _ _ _
# 3. Try-Catch for when assembler doesn't work (using line number to tell you where error is)
#
# PART II: ASSEMBLE CODE ##################################################
# 1. Start rewriting problems #18 & 19 into proper assembly code given our constraints
# 2. Run it through assembler, generate two output files output_18.txt and output_19.txt
# 3. Repeat for problem #17

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

    # halt (x type)
    if wordCount == 1:
        op = getOp(words[0])
        theOutputFile.write(format(op, 'b').zfill(4))   #b means write in binary
        theOutputFile.write(format(0, 'b').zfill(5))
        addComment()

    # IJ or X types
    if wordCount == 2:
        op = getOp(words[0])
        theOutputFile.write(format(op, 'b').zfill(4))
        #
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

    # R and H types
    if wordCount == 3:
        # If R Type
        op = getOp(words[0])
        reg1 = registers[words[1]]
        reg2 = registers[words[2]]
        theOutputFile.write(format(op, 'b').zfill(4))
        theOutputFile.write(format(reg1, 'b').zfill(3))
        theOutputFile.write(format(reg2, 'b').zfill(2))
        addComment()

    # F types
    if wordCount == 4: # Shift Op
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
    print("Ren Jie Shi's Stupid Simple Python Assembler:\n")
    print("Beginning Assembly now!")
    with open('SampleAsm.s') as theInputFile, open('machineCode.txt', 'w') as theOutputFile:
        lineCount = 1
        for line in theInputFile:
            print "Assembling line %d" % lineCount
            # print line
            words = line.split()
            # print words
            try
            assembleMachineCode(words, theOutputFile)
            lineCount += 1
