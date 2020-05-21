ASSUMPTIONS:

1. There should be nothing other than .text and .data on a line.
2. There must be commas in instruction.
3. No space before comma in an instruction.
4. Instructon label is written in the same line as the instruction itself. Similarly for variable name.
5. .asciiz variables are enclosed in ""
6. Put no ':' in comments.
7. Elements of array are seperated by ' ', not by ','.

FOR-REFERENCE:

1. Has support for binary and hex values. They begin with 0x,0b.
2. After string variable, one byte in memory is left vacant.
3. Code segment is stored as unsigned bytes in memory.
4. Immediate value in I format is < = 2^11-1 because we are using signed representation. 
5. In auipc and lui, only positive imm field accepted(range:[0,2^20-1]), just like in Venus.
6. Label name cannot begin with a digit, and cannot contain any ()



