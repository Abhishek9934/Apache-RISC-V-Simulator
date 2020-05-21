
import lexical_analyzer
from Instruction_index import *

instruct_list, data_list = lexical_analyzer.main()

fileObject = open("MachineCode.txt","w+")

def binary_to_hex(substring):
    if substring == '0000':     return '0'
    if substring == '0001':     return '1'
    if substring == '0010':     return '2'
    if substring == '0011':     return '3'
    if substring == '0100':     return '4'
    if substring == '0101':     return '5'
    if substring == '0110':     return '6'
    if substring == '0111':     return '7'
    if substring == '1000':     return '8'
    if substring == '1001':     return '9'
    if substring == '1010':     return 'a'
    if substring == '1011':     return 'b'
    if substring == '1100':     return 'c'
    if substring == '1101':     return 'd'
    if substring == '1110':     return 'e'
    if substring == '1111':     return 'f'

def hex_to_binary(char):
    if char == '0':     return '0000'
    if char == '1':     return '0001'
    if char == '2':     return '0010'
    if char == '3':     return '0011'
    if char == '4':     return '0100'
    if char == '5':     return '0101'
    if char == '6':     return '0110'
    if char == '7':     return '0111'
    if char == '8':     return '1000'
    if char == '9':     return '1001'
    if char == 'a':     return '1010'
    if char == 'b':     return '1011'
    if char == 'c':     return '1100'
    if char == 'd':     return '1101'
    if char == 'e':     return '1110'
    if char == 'f':     return '1111'

for VAR in data_list:
    fileObject.write(VAR.address+" ")
    fileObject.write(VAR.value+"\n")

fileObject.write("\n\n")

MC_code_binary = ""
MC_code='0x'
for command in instruct_list:
    if command.operation != '_':  fileObject.write(command.address+" ")
    if(command.operation=='add' or command.operation=='and' or command.operation=='or' or command.operation=='sll' or
       command.operation=='slt' or command.operation=='sra' or command.operation=='srl' or command.operation=='sub' or
       command.operation=='xor' or command.operation=='mul' or command.operation=='div' or command.operation=='rem'):   # R-format
        MC_code_binary += (funct7[command.operation]
                     + (format(command.reg3,'#07b')[2:]) + (format(command.reg2,'#07b')[2:])
                     + (funct3[command.operation])[2:] + (format(command.reg1,'#07b')[2:])
                     + (opcode[command.operation])[2:])
        #print(MC_code_binary)
        MC_code += (binary_to_hex(MC_code_binary[2:6]) + binary_to_hex(MC_code_binary[6:10]) +
                    binary_to_hex(MC_code_binary[10:14]) + binary_to_hex(MC_code_binary[14:18]) +
                    binary_to_hex(MC_code_binary[18:22]) + binary_to_hex(MC_code_binary[22:26]) +
                    binary_to_hex(MC_code_binary[26:30]) + binary_to_hex(MC_code_binary[30:34]))

        fileObject.write(MC_code+"\n")
        MC_code_binary=""
        MC_code='0x'

    elif (command.operation == 'addi' or command.operation == 'andi' or command.operation == 'ori' or command.operation == 'lb' or
            command.operation == 'ld' or command.operation == 'lh' or command.operation == 'lw' or command.operation == 'jalr'):   # I-format
        if command.immediate >= 0:
            SIC = format(command.immediate, '#014b')
        else:
            SIC = ((command.immediate*-1) ^ 0xfff) + 1
            SIC = format(SIC, '#014b')
        MC_code_binary += (SIC + (format(command.reg2,'#07b')[2:])
                            + (funct3[command.operation])[2:] + (format(command.reg1,'#07b')[2:])
                            + (opcode[command.operation])[2:])
        MC_code += (binary_to_hex(MC_code_binary[2:6]) + binary_to_hex(MC_code_binary[6:10]) +
                    binary_to_hex(MC_code_binary[10:14]) + binary_to_hex(MC_code_binary[14:18]) +
                    binary_to_hex(MC_code_binary[18:22]) + binary_to_hex(MC_code_binary[22:26]) +
                    binary_to_hex(MC_code_binary[26:30]) + binary_to_hex(MC_code_binary[30:34]))

        fileObject.write(MC_code+"\n")
        MC_code_binary = ""
        MC_code = '0x'

    elif (command.operation == 'sb' or command.operation == 'sw' or command.operation == 'sd' or command.operation == 'sh'):  # S-format
        if command.immediate >= 0:
            SIC = command.immediate
        else:
            SIC = ((command.immediate*-1) ^ 0xfff) + 1
        immed = format(SIC, '#014b')

        MC_code_binary += ('0b' + immed[2:9] + (format(command.reg1,'#07b')[2:]) + (format(command.reg2,'#07b')[2:]) +
                           (funct3[command.operation])[2:] + immed[9:] + (opcode[command.operation])[2:])
        MC_code += (binary_to_hex(MC_code_binary[2:6]) + binary_to_hex(MC_code_binary[6:10]) +
                    binary_to_hex(MC_code_binary[10:14]) + binary_to_hex(MC_code_binary[14:18]) +
                    binary_to_hex(MC_code_binary[18:22]) + binary_to_hex(MC_code_binary[22:26]) +
                    binary_to_hex(MC_code_binary[26:30]) + binary_to_hex(MC_code_binary[30:34]))

        fileObject.write(MC_code+"\n")
        MC_code_binary = ""
        MC_code = '0x'

    elif (command.operation == 'beq' or command.operation == 'bne' or command.operation == 'bge' or command.operation == 'blt'):  # SB-format
        NEXT_INT = command.jumptolabel
        CURRENT_ADDRESS = command.address
        for i in range(len(instruct_list)):
            if instruct_list[i].label == NEXT_INT:
                NEXT_ADD_HEX = instruct_list[i].address
                break
        APJ = int(NEXT_ADD_HEX,16) - int(CURRENT_ADDRESS,16)
        if APJ >= 0:    NEXT_ADD = format(APJ, "#015b")[2:]
        else:
            APJ = ((APJ*-1)^0b1111111111111) + 1
            NEXT_ADD = format(APJ, "#015b")[2:]

        MC_code_binary += ('0b' + NEXT_ADD[0] + NEXT_ADD[2:8] + (format(command.reg2,'#07b')[2:]) +
                           (format(command.reg1,'#07b')[2:]) + (funct3[command.operation])[2:] + NEXT_ADD[8:12] +
                            NEXT_ADD[1] + (opcode[command.operation])[2:])
        MC_code += (binary_to_hex(MC_code_binary[2:6]) + binary_to_hex(MC_code_binary[6:10]) +
                    binary_to_hex(MC_code_binary[10:14]) + binary_to_hex(MC_code_binary[14:18]) +
                    binary_to_hex(MC_code_binary[18:22]) + binary_to_hex(MC_code_binary[22:26]) +
                    binary_to_hex(MC_code_binary[26:30]) + binary_to_hex(MC_code_binary[30:34]))

        fileObject.write(MC_code+"\n")
        MC_code_binary = ""
        MC_code = '0x'

    elif command.operation == 'jal':     # UJ format
        NEXT_INT = command.jumptolabel
        CURRENT_ADDRESS = command.address
        for i in range(len(instruct_list)):
            if instruct_list[i].label == NEXT_INT:
                NEXT_ADD_HEX = instruct_list[i].address
                break
        APJ = int(NEXT_ADD_HEX,16) - int(CURRENT_ADDRESS,16)
        if APJ >= 0:    NEXT_ADD = format(APJ, "#023b")[2:]
        else:
            APJ = ((APJ * -1) ^ 0b111111111111111111111) + 1
            NEXT_ADD = format(APJ, "#023b")[2:]

        MC_code_binary = ('0b' + NEXT_ADD[0] + NEXT_ADD[10:20] + NEXT_ADD[9] + NEXT_ADD[1:9] +
                           (format(command.reg1, '#07b')[2:]) + (opcode[command.operation])[2:])
        MC_code += (binary_to_hex(MC_code_binary[2:6]) + binary_to_hex(MC_code_binary[6:10]) +
                    binary_to_hex(MC_code_binary[10:14]) + binary_to_hex(MC_code_binary[14:18]) +
                    binary_to_hex(MC_code_binary[18:22]) + binary_to_hex(MC_code_binary[22:26]) +
                    binary_to_hex(MC_code_binary[26:30]) + binary_to_hex(MC_code_binary[30:34]))

        fileObject.write(MC_code+"\n")
        MC_code_binary = ""
        MC_code = '0x'

    elif command.operation == 'auipc' or command.operation == 'lui':      # U format
        immed = format(command.immediate, '#022b')
        immed += '000000000000'
        MC_code_binary = ('0b' + immed[2:22] + (format(command.reg1, '#07b')[2:]) + (opcode[command.operation])[2:])
        MC_code += (binary_to_hex(MC_code_binary[2:6]) + binary_to_hex(MC_code_binary[6:10]) +
                    binary_to_hex(MC_code_binary[10:14]) + binary_to_hex(MC_code_binary[14:18]) +
                    binary_to_hex(MC_code_binary[18:22]) + binary_to_hex(MC_code_binary[22:26]) +
                    binary_to_hex(MC_code_binary[26:30]) + binary_to_hex(MC_code_binary[30:34]))

        fileObject.write(MC_code+"\n")
        MC_code_binary = ""
        MC_code = '0x'


fileObject.close()

















