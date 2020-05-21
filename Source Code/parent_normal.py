import memory_normal   # DON'T import as *
import EXEC_data_normal
import register_file

def hex_to_binary(char):
    if char == '0':     return '0000'
    elif char == '1':     return '0001'
    elif char == '2':     return '0010'
    elif char == '3':     return '0011'
    elif char == '4':     return '0100'
    elif char == '5':     return '0101'
    elif char == '6':     return '0110'
    elif char == '7':     return '0111'
    elif char == '8':     return '1000'
    elif char == '9':     return '1001'
    elif char == 'a':     return '1010'
    elif char == 'b':     return '1011'
    elif char == 'c':     return '1100'
    elif char == 'd':     return '1101'
    elif char == 'e':     return '1110'
    elif char == 'f':     return '1111'

file_object = open("MachineCode.txt", "r")
mc_code = file_object.readlines()

for i in range(len(mc_code)):
    if (mc_code[i])[-1] == '\n':   mc_code[i] = mc_code[i][:-1]
# print(mc_code)

i = 0
for i in range(len(mc_code)):
    if mc_code[i] == '':        break

    value = ""
    j = mc_code[i].find(' ')
    address = int(mc_code[i][:j],16)
    if mc_code[i][j+1] == '"':
        type = 0    # str
        value = (mc_code[i])[j+2:-1]
    elif mc_code[i][j+1] == 'b':
        type = 1    # byte
        value = mc_code[i][j+3:-1]+' '
        # length = 0
        # for f in range(j+4,len(mc_code[i])):
        #     if mc_code[i][f] == ' ':   length += 1
    elif mc_code[i][j+1] == 'w':
        type = 2    # word
        value = mc_code[i][j+3:-1] + ' '
    elif mc_code[i][j+1] == 'h':
        type = 3    # half-word
        value = mc_code[i][j+3:-1] + ' '
    elif mc_code[i][j+1] == 'd':
        type = 4    # double word
        value = mc_code[i][j+3:-1] + ' '

    EXEC_data_normal.execute_data(value,type,address)

for i in range(i+2,len(mc_code)):
    j = mc_code[i].find(' ')
    address = (mc_code[i])[:j]
    k = (mc_code[i])[j+1:]
    binary_equivalent = hex_to_binary(k[2]) + hex_to_binary(k[3]) + hex_to_binary(k[4]) + hex_to_binary(k[5]) + hex_to_binary(k[6]) + hex_to_binary(k[7]) + hex_to_binary(k[8]) + hex_to_binary(k[9])
    # print(binary_equivalent)
    memory_normal.write_code_line_to_mem(int(address,16), binary_equivalent)



# register_file.print_register(0)
# memory_normal.print_all_memory()
# print(memory_normal.code_stop)
# print(hex(memory_normal.data_stop))
# print(memory_normal.read_byte_from_mem(int("0x0",16)))












