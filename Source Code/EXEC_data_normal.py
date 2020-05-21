import memory_normal      # don't import it as *

def execute_data(value, type, address):     # value: string, type: int, address:string
    # 0: str,1: byte, 2: word, 3: half-word, 4: double-word
    if type == 0:   # ascii
        i = 0
        for i in range(len(value)):
            memory_normal.write_byte_to_mem(address+i,ord(value[i]))   # sending the ASCII value
        memory_normal.write_byte_to_mem(address+i+1,0)
    elif type == 1:     # byte
        j = 0
        CO = 0
        for i in range(len(value)):
            if value[i] == ' ':
                if  value[j] == '-':
                    if len(value[j:i]) == 2:     memory_normal.write_byte_to_mem(address+CO, int(value[j:i]),1)
                    elif value[j+1] == '0' and value[j+2] == 'x':   memory_normal.write_byte_to_mem(address+CO, int(value[j:i], 16),1)
                    elif value[j+1] == '0' and value[j+2] == 'b':   memory_normal.write_byte_to_mem(address+CO, int(value[j:i], 2),1)
                    else:                               memory_normal.write_byte_to_mem(address+CO, int(value[j:i]),1)
                else:
                    if len(value[j:i]) == 1:     memory_normal.write_byte_to_mem(address+CO, int(value[j:i]),1)
                    elif value[j] == '0' and value[j+1] == 'x':   memory_normal.write_byte_to_mem(address+CO, int(value[j:i], 16),1)
                    elif value[j] == '0' and value[j+1] == 'b':   memory_normal.write_byte_to_mem(address+CO, int(value[j:i], 2),1)
                    else:                               memory_normal.write_byte_to_mem(address+CO, int(value[j:i]),1)
                CO += 1
                j = i+1

    elif type == 3:     # half-word
        j = 0
        CO = 0
        for i in range(len(value)):
            if value[i] == ' ':
                if value[j] == '-':
                    if len(value[j:i]) == 2:
                        memory_normal.write_hword_to_mem(address + CO, int(value[j:i]))
                    elif value[j + 1] == '0' and value[j + 2] == 'x':
                        memory_normal.write_hword_to_mem(address + CO, int(value[j:i], 16))
                    elif value[j + 1] == '0' and value[j + 2] == 'b':
                        memory_normal.write_hword_to_mem(address + CO, int(value[j:i], 2))
                    else:
                        memory_normal.write_hword_to_mem(address + CO, int(value[j:i]))
                else:
                    if len(value[j:i]) == 1:
                        memory_normal.write_hword_to_mem(address + CO, int(value[j:i]))
                    elif value[j] == '0' and value[j + 1] == 'x':
                        memory_normal.write_hword_to_mem(address + CO, int(value[j:i], 16))
                    elif value[j] == '0' and value[j + 1] == 'b':
                        memory_normal.write_hword_to_mem(address + CO, int(value[j:i], 2))
                    else:
                        memory_normal.write_hword_to_mem(address + CO, int(value[j:i]))
                CO += 2
                j = i + 1

    elif type == 2:     # word
        j = 0
        CO = 0
        for i in range(len(value)):
            if value[i] == ' ':
                if value[j] == '-':
                    if len(value[j:i]) == 2:
                        memory_normal.write_word_to_mem(address + CO, int(value[j:i]))
                    elif value[j + 1] == '0' and value[j + 2] == 'x':
                        memory_normal.write_word_to_mem(address + CO, int(value[j:i], 16))
                    elif value[j + 1] == '0' and value[j + 2] == 'b':
                        memory_normal.write_word_to_mem(address + CO, int(value[j:i], 2))
                    else:
                        memory_normal.write_word_to_mem(address + CO, int(value[j:i]))
                else:
                    if len(value[j:i]) == 1:
                        memory_normal.write_word_to_mem(address + CO, int(value[j:i]))
                    elif value[j] == '0' and value[j + 1] == 'x':
                        memory_normal.write_word_to_mem(address + CO, int(value[j:i], 16))
                    elif value[j] == '0' and value[j + 1] == 'b':
                        memory_normal.write_word_to_mem(address + CO, int(value[j:i], 2))
                    else:
                        memory_normal.write_word_to_mem(address + CO, int(value[j:i]))
                CO += 4
                j = i + 1

    elif type == 4:     # double-word
        j = 0
        CO = 0
        for i in range(len(value)):
            if value[i] == ' ':
                if value[j] == '-':
                    if len(value[j:i]) == 2:
                        memory_normal.write_dword_to_mem(address + CO, int(value[j:i]))
                    elif value[j + 1] == '0' and value[j + 2] == 'x':
                        memory_normal.write_dword_to_mem(address + CO, int(value[j:i], 16))
                    elif value[j + 1] == '0' and value[j + 2] == 'b':
                        memory_normal.write_dword_to_mem(address + CO, int(value[j:i], 2))
                    else:
                        memory_normal.write_dword_to_mem(address + CO, int(value[j:i]))
                else:
                    if len(value[j:i]) == 1:
                        memory_normal.write_dword_to_mem(address + CO, int(value[j:i]))
                    elif value[j] == '0' and value[j + 1] == 'x':
                        memory_normal.write_dword_to_mem(address + CO, int(value[j:i], 16))
                    elif value[j] == '0' and value[j + 1] == 'b':
                        memory_normal.write_dword_to_mem(address + CO, int(value[j:i], 2))
                    else:
                        memory_normal.write_dword_to_mem(address + CO, int(value[j:i]))
                CO += 8
                j = i + 1








