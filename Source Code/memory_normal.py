data_stop = 0x10000000
# stack_start = 0x7ffffffc
code_stop = 0x0

memory_map = {}     # byte addressable
# Each byte of memory stores an integer decimal value(positive or negative)
# address is int

def write_code_line_to_mem(address, code):          # code address is stored as unsigned integer in each byte
    memory_map[address] = int(code[0:8],2)
    memory_map[address+1] = int(code[8:16], 2)
    memory_map[address+2] = int(code[16:24], 2)
    memory_map[address+3] = int(code[24:], 2)
    global code_stop
    # print(code_stop)
    if address == code_stop:    code_stop += 4

def read_code_line_from_mem(address):       # returns 32-bit binary string
    return format(memory_map[address],"#010b")[2:] + format(memory_map[address+1],"#010b")[2:] + format(memory_map[address+2],"#010b")[2:] + format(memory_map[address+3],"#010b")[2:]

def write_byte_to_mem(address, value,swer=0):          # 'value' is int always
    memory_map[address] = value
    global data_stop
    if address == data_stop:    data_stop += 1
    
def write_hword_to_mem(address, v):     # value is int
    ER1 = 0
    ER2 = 0
    global data_stop
    if address == data_stop:    data_stop += 2
    if v > 0:
        s = format(v, "#018b")[2:]
        s1 = s[0:8]
        s2 = s[8:]
        if s1[0] == '0':
            write_byte_to_mem(address, int(s1, 2))
            ER1 = int(s1, 2)
        else:
            c = int(s1, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address, c * -1)
            ER1 = c * -1
        if s2[0] == '0':
            write_byte_to_mem(address + 1, int(s2, 2))
            ER2 = int(s2, 2)
        else:
            c = int(s2, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address + 1, c * -1)
            ER2=c * -1
    elif v == 0:
        write_byte_to_mem(address, 0)
        write_byte_to_mem(address + 1, 0)
        ER1=0
        ER2=0
    else:
        s = format(v, "#019b")[3:]
        C = int(s, 2)
        C = (0xffff ^ C) + 1
        s = format(C, "#018b")[2:]
        s1 = s[0:8]
        s2 = s[8:]
        if s1[0] == '0':
            write_byte_to_mem(address, int(s1, 2))
            ER1=int(s1, 2)
        else:
            c = int(s1, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address, c * -1)
            ER1=c * -1
        if s2[0] == '0':
            write_byte_to_mem(address + 1, int(s2, 2))
            ER2=int(s2, 2)
        else:
            c = int(s2, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address + 1, c * -1)
            ER2=c * -1


def write_word_to_mem(address, v):
    ER1=ER2=ER3=ER4=0
    global data_stop
    if address == data_stop:    data_stop += 4
    if v > 0:
        s = format(v, "#034b")[2:]
        s1 = s[0:8]
        s2 = s[8:16]
        s3 = s[16:24]
        s4 = s[24:]
        if s1[0] == '0':
            write_byte_to_mem(address, int(s1, 2))
            ER1=int(s1, 2)
        else:
            c = int(s1, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address, c * -1)
            ER1=c * -1
        if s2[0] == '0':
            write_byte_to_mem(address + 1, int(s2, 2))
            ER2=int(s2, 2)
        else:
            c = int(s2, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address + 1, c * -1)
            ER2=c * -1
        if s3[0] == '0':
            write_byte_to_mem(address + 2, int(s3, 2))
            ER3=int(s3, 2)
        else:
            c = int(s3, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address + 2, c * -1)
            ER3=c * -1
        if s4[0] == '0':
            write_byte_to_mem(address + 3, int(s4, 2))
            ER4=int(s4, 2)
        else:
            c = int(s4, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address + 3, c * -1)
            ER4=c * -1
    elif v == 0:
        write_byte_to_mem(address, 0)
        write_byte_to_mem(address + 1, 0)
        write_byte_to_mem(address + 2, 0)
        write_byte_to_mem(address + 3, 0)
        ER1=ER4=ER2=ER3=0
    else:
        s = format(v, "#035b")[3:]
        C = int(s, 2)
        C = (0xffffffff ^ C) + 1
        s = format(C, "#034b")[2:]
        s1 = s[0:8]
        s2 = s[8:16]
        s3 = s[16:24]
        s4 = s[24:]
        if s1[0] == '0':
            write_byte_to_mem(address, int(s1, 2))
            ER1=int(s1, 2)
        else:
            c = int(s1, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address, c * -1)
            ER1=c * -1
        if s2[0] == '0':
            write_byte_to_mem(address + 1, int(s2, 2))
            ER2=int(s2, 2)
        else:
            c = int(s2, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address + 1, c * -1)
            ER2=c * -1
        if s3[0] == '0':
            write_byte_to_mem(address + 2, int(s3, 2))
            ER3=int(s3, 2)
        else:
            c = int(s3, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address + 2, c * -1)
            ER3=c * -1
        if s4[0] == '0':
            write_byte_to_mem(address + 3, int(s4, 2))
            ER4=int(s4, 2)
        else:
            c = int(s4, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address + 3, c * -1)
            ER4=c * -1


def write_dword_to_mem(address, v):
    ER1=ER2=ER3=ER4=ER5=ER6=ER7=ER8=0
    global data_stop
    if address == data_stop:    data_stop += 8
    if v > 0:
        s = format(v, "#066b")[2:]
        s1 = s[0:8]
        s2 = s[8:16]
        s3 = s[16:24]
        s4 = s[24:32]
        s5 = s[32:40]
        s6 = s[40:48]
        s7 = s[48:56]
        s8 = s[56:]
        if s1[0] == '0':
            write_byte_to_mem(address, int(s1, 2))
            ER1=int(s1, 2)
        else:
            c = int(s1, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address, c * -1)
            ER1=c * -1
        if s2[0] == '0':
            write_byte_to_mem(address + 1, int(s2, 2))
            ER2=int(s2, 2)
        else:
            c = int(s2, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address + 1, c * -1)
            ER2=c * -1
        if s3[0] == '0':
            write_byte_to_mem(address + 2, int(s3, 2))
            ER3=int(s3, 2)
        else:
            c = int(s3, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address + 2, c * -1)
            ER3=c * -1
        if s4[0] == '0':
            write_byte_to_mem(address + 3, int(s4, 2))
            ER4=int(s4, 2)
        else:
            c = int(s4, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address + 3, c * -1)
            ER4=c * -1
        if s5[0] == '0':
            write_byte_to_mem(address + 4, int(s5, 2))
            ER5=int(s5, 2)
        else:
            c = int(s5, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address + 4, c * -1)
            ER5=c * -1
        if s6[0] == '0':
            write_byte_to_mem(address + 5, int(s6, 2))
            ER6=int(s6, 2)
        else:
            c = int(s6, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address + 5, c * -1)
            ER6=c * -1
        if s7[0] == '0':
            write_byte_to_mem(address + 6, int(s7, 2))
            ER7=int(s7, 2)
        else:
            c = int(s7, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address + 6, c * -1)
            ER7=c * -1
        if s8[0] == '0':
            write_byte_to_mem(address + 7, int(s8, 2))
            ER8=int(s8, 2)
        else:
            c = int(s8, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address + 7, c * -1)
            ER8=c * -1
    elif v == 0:
        write_byte_to_mem(address, 0)
        write_byte_to_mem(address + 1, 0)
        write_byte_to_mem(address + 2, 0)
        write_byte_to_mem(address + 3, 0)
        write_byte_to_mem(address + 4, 0)
        write_byte_to_mem(address + 5, 0)
        write_byte_to_mem(address + 6, 0)
        write_byte_to_mem(address + 7, 0)
        ER4=ER3=ER2=ER1=ER5=ER6=ER7=ER8=0
    else:
        s = format(v, "#067b")[3:]
        C = int(s, 2)
        C = (0xffffffffffffffff ^ C) + 1
        s = format(C, "#066b")[2:]
        s1 = s[0:8]
        s2 = s[8:16]
        s3 = s[16:24]
        s4 = s[24:32]
        s5 = s[32:40]
        s6 = s[40:48]
        s7 = s[48:56]
        s8 = s[56:]
        if s1[0] == '0':
            write_byte_to_mem(address, int(s1, 2))
            ER1=int(s1, 2)
        else:
            c = int(s1, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address, c * -1)
            ER1=c * -1
        if s2[0] == '0':
            write_byte_to_mem(address + 1, int(s2, 2))
            ER2=int(s2, 2)
        else:
            c = int(s2, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address + 1, c * -1)
            ER2=c * -1
        if s3[0] == '0':
            write_byte_to_mem(address + 2, int(s3, 2))
            ER3=int(s3, 2)
        else:
            c = int(s3, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address + 2, c * -1)
            ER3=c * -1
        if s4[0] == '0':
            write_byte_to_mem(address + 3, int(s4, 2))
            ER4=int(s4, 2)
        else:
            c = int(s4, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address + 3, c * -1)
            ER4=c * -1
        if s5[0] == '0':
            write_byte_to_mem(address + 4, int(s5, 2))
            ER5=int(s5, 2)
        else:
            c = int(s5, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address + 4, c * -1)
            ER5=c * -1
        if s6[0] == '0':
            write_byte_to_mem(address + 5, int(s6, 2))
            ER6=int(s6, 2)
        else:
            c = int(s6, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address + 5, c * -1)
            ER6=c * -1
        if s7[0] == '0':
            write_byte_to_mem(address + 6, int(s7, 2))
            ER7=int(s7, 2)
        else:
            c = int(s7, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address + 6, c * -1)
            ER7=c * -1
        if s8[0] == '0':
            write_byte_to_mem(address + 7, int(s8, 2))
            ER8=int(s8, 2)
        else:
            c = int(s8, 2)
            c = (0xff ^ c) + 1
            write_byte_to_mem(address + 7, c * -1)
            ER8=c * -1


def print_all_memory():
    for address,value in memory_map.items():
        print(f"{hex(address)}  {value}")

def read_byte_from_mem(address):        # address is int
    return memory_map[address]

def read_hword_from_mem(address):
    i1 = memory_map[address]
    i2 = memory_map[address+1]
    if i1 >=0:
        s1 = format(i1, "#010b")[2:]
    else:
        i1 = (i1-1) ^ 0xff
        s1 = format(i1, "010b")[2:]
    if i2 >=0:
        s2 = format(i2, "#010b")[2:]
    else:
        i2 = (i2-1) ^ 0xff
        s2 = format(i2, "010b")[2:]
    s = s1 + s2
    i = int(s,2)
    if s[0] == '0':  return i
    elif s[0] == '1':
        i = (i-1) ^ 0xffff
        return i*-1

def read_word_from_mem(address):
    i1 = memory_map[address]
    i2 = memory_map[address + 1]
    i3 = memory_map[address + 2]
    i4 = memory_map[address + 3]
    if i1 >= 0:
        s1 = format(i1, "#010b")[2:]
    else:
        i1 = (i1 - 1) ^ 0xff
        s1 = format(i1, "010b")[2:]
    if i2 >= 0:
        s2 = format(i2, "#010b")[2:]
    else:
        i2 = (i2 - 1) ^ 0xff
        s2 = format(i2, "010b")[2:]
    if i3 >= 0:
        s3 = format(i3, "#010b")[2:]
    else:
        i3 = (i3 - 1) ^ 0xff
        s3 = format(i3, "010b")[2:]
    if i4 >= 0:
        s4 = format(i4, "#010b")[2:]
    else:
        i4 = (i4 - 1) ^ 0xff
        s4 = format(i4, "010b")[2:]
    s = s1 + s2 + s3 + s4
    i = int(s, 2)
    if s[0] == '0':
        return i
    elif s[0] == '1':
        i = (i - 1) ^ 0xffffffff
        return i * -1

def read_dword_from_mem(address):
    i1 = memory_map[address]
    i2 = memory_map[address + 1]
    i3 = memory_map[address + 2]
    i4 = memory_map[address + 3]
    i5 = memory_map[address + 4]
    i6 = memory_map[address + 5]
    i7 = memory_map[address + 6]
    i8 = memory_map[address + 7]
    if i1 >= 0:
        s1 = format(i1, "#010b")[2:]
    else:
        i1 = (i1 - 1) ^ 0xff
        s1 = format(i1, "010b")[2:]
    if i2 >= 0:
        s2 = format(i2, "#010b")[2:]
    else:
        i2 = (i2 - 1) ^ 0xff
        s2 = format(i2, "010b")[2:]
    if i3 >= 0:
        s3 = format(i3, "#010b")[2:]
    else:
        i3 = (i3 - 1) ^ 0xff
        s3 = format(i3, "010b")[2:]
    if i4 >= 0:
        s4 = format(i4, "#010b")[2:]
    else:
        i4 = (i4 - 1) ^ 0xff
        s4 = format(i4, "010b")[2:]
    if i5 >= 0:
        s5 = format(i5, "#010b")[2:]
    else:
        i5 = (i5 - 1) ^ 0xff
        s5 = format(i5, "010b")[2:]
    if i6 >= 0:
        s6 = format(i6, "#010b")[2:]
    else:
        i6 = (i6 - 1) ^ 0xff
        s6 = format(i6, "010b")[2:]
    if i7 >= 0:
        s7 = format(i7, "#010b")[2:]
    else:
        i7 = (i7 - 1) ^ 0xff
        s7 = format(i7, "010b")[2:]
    if i8 >= 0:
        s8 = format(i8, "#010b")[2:]
    else:
        i8 = (i8 - 1) ^ 0xff
        s8 = format(i8, "010b")[2:]
    s = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8
    i = int(s, 2)
    if s[0] == '0':
        return i
    elif s[0] == '1':
        i = (i - 1) ^ 0xffffffffffffffff
        return i * -1


def print_code_into_apache():
    fileObject = open('Memory_file.txt', 'a')
    address_avail = []
    for i in memory_map.keys():
        if i < 0x10000000:     address_avail.append(i)
    address_avail = sorted(address_avail)
    length = len(address_avail)
    i = 0
    while i < length:
        fileObject.write(f'\n{hex(address_avail[i])}\t\t{memory_map[address_avail[i]]}\t{memory_map[address_avail[i+1]]}\t{memory_map[address_avail[i+2]]}\t{memory_map[address_avail[i+3]]}')
        i += 4

def print_mem_into_apache():    # for address > 0x10000000
    fileObject = open('Memory_file.txt', 'w+')
    address_avail = []
    for i in memory_map.keys():
        if i >= 0x10000000:        address_avail.append(i)
    address_avail = sorted(address_avail)
    length = len(address_avail)
    i = 0
    while i < length:
        if i+3 < length and address_avail[i]==address_avail[i+1]-1 and address_avail[i]==address_avail[i+2]-2 and address_avail[i]==address_avail[i+3]-3:
            if address_avail[i]>=0x70000000:  fileObject.write(f'\n{hex(address_avail[i])}\t\t{memory_map[address_avail[i]]}\t{memory_map[address_avail[i+1]]}\t{memory_map[address_avail[i+2]]}\t{memory_map[address_avail[i+3]]}')
            else:   fileObject.write(f'\n{hex(address_avail[i])}\t{memory_map[address_avail[i]]}\t{memory_map[address_avail[i+1]]}\t{memory_map[address_avail[i+2]]}\t{memory_map[address_avail[i+3]]}')
            i += 4

        elif (i+3 >= length or address_avail[i+3] != address_avail[i]+3) and i+2 < length and address_avail[i]==address_avail[i+1]-1 and address_avail[i]==address_avail[i+2]-2:
            if address_avail[i]>=0x70000000:  fileObject.write(f'\n{hex(address_avail[i])}\t\t{memory_map[address_avail[i]]}\t{memory_map[address_avail[i+1]]}\t{memory_map[address_avail[i+2]]}')
            else:   fileObject.write(f'\n{hex(address_avail[i])}\t{memory_map[address_avail[i]]}\t{memory_map[address_avail[i+1]]}\t{memory_map[address_avail[i+2]]}')
            i += 3

        elif (i+2 >= length or address_avail[i+2] != address_avail[i]+2) and i+1 < length and address_avail[i]==address_avail[i+1]-1:
            if address_avail[i]>=0x70000000:  fileObject.write(f'\n{hex(address_avail[i])}\t\t{memory_map[address_avail[i]]}\t{memory_map[address_avail[i+1]]}')
            else:   fileObject.write(f'\n{hex(address_avail[i])}\t{memory_map[address_avail[i]]}\t{memory_map[address_avail[i+1]]}')
            i += 2

        elif i+1 >= length or address_avail[i+1] != address_avail[i]+1:
            if address_avail[i] >= 0x70000000:   fileObject.write(f'\n{hex(address_avail[i])}\t\t{memory_map[address_avail[i]]}')
            else:       fileObject.write(f'\n{hex(address_avail[i])}\t{memory_map[address_avail[i]]}')
            i += 1






