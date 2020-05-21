import lexical_analyzer
import Instruct_nd_Variable_Names
import Instruction_index

def main():
    instruct_list, data_list = lexical_analyzer.main()
    error = "noerror"
    errorline = 0
    # print(*instruct_list,sep='\n')
    # print(Instruct_nd_Variable_Names.Instruct_names)
    CD=0
    for j in data_list:
        CD+=1
        if j.type != '.byte' and j.type != '.word' and j.type != '.half' and j.type != '.dword' and j.type != '.asciz':
            error = "Check your assembler directive- .asciz .byte .word .half .dword are supported for data"
            return error,CD
        if (j.value[0] == 'w' or j.value[0] == 'h' or j.value[0] == 'b' or j.value[0] == 'd') and (j.value).find(',')!=-1:
            error = "In case of multiple values in .word .byte .dword .half, seperate them by space not by comma"
            return error,CD

    for i in instruct_list:
        errorline += 1
        if (not i.operation in Instruction_index.opcode) and i.operation != '_':
            error = "Command not supported"
            break

        if i.operation == 'andi' or i.operation == 'addi' or i.operation == 'ori' or i.operation == 'lb' or i.operation == 'ld' or i.operation == 'lh' or i.operation == 'lw' or i.operation == 'jalr':
            if i.reg3 != -1:
                error = "immediate value missing in I-type instruction"
            elif i.immediate > 2047 or i.immediate < -2048:
                error = "immediate value not in range in I-type instruction"
            if i.reg1 == -1 or i.reg2 == -1:
                error = "2 registers required for I- type instruction"


        elif i.operation == 'sb' or i.operation == 'sw' or i.operation == 'sd' or i.operation == 'sh':
            if i.reg3 != -1:
                error = "immediate value missing in S-type instruction"
            elif i.immediate > 2047 or i.immediate < -2048:
                error = "immediate value not in range in S-type instruction"
            if i.reg1 == -1 or i.reg2 == -1:
                error = "2 registers required for S- type instruction"


        elif i.operation == 'beq' or i.operation == 'bne' or i.operation == 'bge' or i.operation == 'blt':
            if not i.jumptolabel:
                error = "jump to label missing in SB-type instruction"
            elif i.jumptolabel not in Instruct_nd_Variable_Names.Instruct_names.keys():
                error = "Jump to label does NOT exist in the program for SB-instruction"
            if i.reg1 == -1 or i.reg2 == -1:
                error = "2 registers required for SB- type instruction"


        elif i.operation == 'auipc' or i.operation == 'lui':
            if i.immediate == 0:
                error = "immediate value is either 0 or missing in U-type instruction"
            elif i.immediate > 524287:
                error = "immediate value not in range in U-type instruction"
            if i.reg1 == -1:
                error = "1 register required for U- type instruction"

        elif i.operation == 'jal':
            if not i.jumptolabel:
                error = "Jump to label is missing in jal"
            elif i.jumptolabel not in Instruct_nd_Variable_Names.Instruct_names.keys():
                error = "Jump to label given in jal instruction,does NOT exist in the program"
            if i.reg1 == -1:
                error = "1 register required for jal instructions"

        elif i.operation == 'and' or i.operation == 'add' or i.operation == 'or' or i.operation == 'sll' or i.operation == 'slt' or i.operation == 'sra' or i.operation == 'srl' or i.operation == 'sub' or i.operation == 'xor' or i.operation == 'mul' or i.operation == 'div' or i.operation == 'rem':
            if i.reg1 == -1 or i.reg2 == -1 or i.reg3 == -1:
                error = "3 register required for R type instructions"


        if error != "noerror":
            break

    return error,errorline


#main()