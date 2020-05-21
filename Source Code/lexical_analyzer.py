import Instruct_nd_Variable_Names
from dataclasses import dataclass

def main():
    def get_index_of_register(REG):
        if REG[0] == 'x':
            return int(REG[1:])
        elif REG == 'zero':
            return 0
        elif REG == 'ra':
            return 1
        elif REG == 'sp':
            return 2
        elif REG == 'gp':
            return 3
        elif REG == 'tp':
            return 4
        elif REG[0] == 't' and '0' <= REG[1] <= '2':
            return 5 + int(REG[1])
        elif REG[0] == 's' and '0' <= REG[1] <= '1':
            return 8 + int(REG[1])
        elif REG[0] == 'a' and '0' <= REG[1] <= '7':
            return 10 + int(REG[1])
        elif REG[0] == 's' and '2' <= REG[1:] <= '11':
            return 16 + int(REG[1:])
        elif REG[0] == 't' and '3' <= REG[1] <= '6':
            return 25 + int(REG[1])

    @dataclass
    class instruction():
        label: str = None
        address: str = None
        operation: str = None
        reg1: int = -1
        reg2: int = -1
        reg3: int = -1
        immediate: int = 0
        directive: str = None
        jumptolabel: str = None

    @dataclass
    class variable():
        name: str = None
        address: str = None
        type: str = None
        value: str = ""

    file = open("codefromeditor.txt", "r")
    data = file.readlines()
    # file.close()
    length = len(data)
    i = 0
    while i < length:
        if data[i] == '\n':
            data[i] = ''
        elif ((data[i])[-1] == '\n'):
            data[i] = data[i][:-1]  # data is a list that stores each individual line

        data[i] = data[i].strip()

        if (data[i] == '' or (data[i])[0] == '#'):
            data.pop(i)
            length -= 1
            continue
        i += 1

    # print(data)  # hence, all the comment lines and new lines are removed from the data-list
    toggle = 0
   
    data_list = []
    instruct_list = []
    add = 0
    ADD = 0x10000000
    CO = 0
    for j in range(len(data)):
        if data[j] == '.data':
            toggle = 1
            continue
        elif data[j] == '.text':
            toggle = 0
            continue
        elif (data[j])[-1] == ':':
            obj = instruction()
            obj.address = hex(add)
            add += 4
            obj.label = (data[j])[:-1]
            obj.operation = '_'  # exit code
            instruct_list.append(obj)
            if obj.label:   Instruct_nd_Variable_Names.add_to_instructnames(obj.label, obj.address)
            continue

        if toggle == 1:
            OBJ = variable()
            rem = ''
            for i in range(len(data[j])):
                if data[j][i] == ':':
                    OBJ.name = data[j][0:i].strip()
                    rem = data[j][i + 1:]
                    break
            if rem == '':   rem = data[j]
            rem = rem.strip()
            instruct = ''
            for i in range(len(rem)):
                if rem[i] == '#':
                    instruct = rem[0:i]
                    break
            if instruct == '': instruct = rem
            for i in range(len(instruct)):
                if instruct[i] == ' ':
                    OBJ.type = instruct[:i]
                    VALUES = instruct[i + 1:]
                    VALUES = VALUES.strip()
                    break
            FG = 0
            if OBJ.type == '.asciz':
                E = VALUES[1:].find('"')
                OBJ.value = '"' + VALUES[1:E + 1] + '"'
                OBJ.address = hex(ADD)
                ADD += len(OBJ.value) - 1
            if OBJ.type == '.byte':
                OBJ.value = 'b '
                for i in range(len(VALUES)):
                    if (VALUES[i] == ' '):
                        OBJ.value += VALUES[FG:i] + ' '
                        FG = i + 1
                        CO += 1
                OBJ.value += VALUES[FG:] + ' '
                OBJ.address = hex(ADD)
                ADD += CO + 1
                FG = 0
                CO = 0
            if OBJ.type == '.half':
                OBJ.value = 'h '
                for i in range(len(VALUES)):
                    if (VALUES[i] == ' '):
                        OBJ.value += VALUES[FG:i] + ' '
                        FG = i + 1
                        CO += 1
                OBJ.value += VALUES[FG:] + ' '
                OBJ.address = hex(ADD)
                ADD += 2 * (CO + 1)
                FG = 0
                CO = 0
            if OBJ.type == '.word':
                OBJ.value = 'w '
                for i in range(len(VALUES)):
                    if (VALUES[i] == ' '):
                        OBJ.value += VALUES[FG:i] + ' '
                        FG = i + 1
                        CO += 1
                OBJ.value += VALUES[FG:] + ' '
                OBJ.address = hex(ADD)
                ADD += 4 * (CO + 1)
                FG = 0
                CO = 0
            if OBJ.type == '.dword':
                OBJ.value = 'd '
                for i in range(len(VALUES)):
                    if (VALUES[i] == ' '):
                        OBJ.value += VALUES[FG:i] + ' '
                        FG = i + 1
                        CO += 1
                OBJ.value += VALUES[FG:] + ' '
                OBJ.address = hex(ADD)
                ADD += 8 * (CO + 1)
                FG = 0
                CO = 0

            data_list.append(OBJ)

        elif toggle == 0:
            obj = instruction()
            obj.address = hex(add)

            for i in range(len(data[j])):
                rem = ''
                instruct = ''
                if (data[j][i] == ':'):
                    obj.label = data[j][0:i].strip()
                    rem = data[j][i + 1:]
                    rem = rem.strip()
                    break
            if (rem == ''): rem = data[j]
            if obj.label:   Instruct_nd_Variable_Names.add_to_instructnames(obj.label,obj.address)
            add += 4

            for i in range(len(rem)):
                if (rem[i] == '#'):
                    instruct = rem[0:i]
                    break
            if (instruct == ''): instruct = rem
            for i in range(len(instruct)):
                if (instruct[i] == ' '):
                    obj.operation = instruct[0:i]
                    reg = instruct[i + 1:]
                    reg = reg.strip()
                    break

            count = 0
            i1 = -1
            for i in range(len(reg)):
                if reg[i] == ',':
                    count += 1
                    if count == 1:  i1 = i
                    if i1 > -1: i2 = i

            if count == 1:
                obj.reg1 = get_index_of_register(reg[:i1].strip())
                r = reg[i1 + 1:].strip()
                if r == 'ra' or r == 'zero' or r == 'sp' or r == 'gp' or r == 'tp' or (
                        r[0] == 'x' and int(r[1:]) < 32 and int(r[1:]) >= 0) or (
                        r[0] == 't' and int(r[1:]) < 7 and int(r[1:]) >= 0) or (
                        r[0] == 's' and int(r[1:]) < 12 and int(r[1:]) >= 0) or (
                        r[0] == 'a' and int(r[1:]) < 8 and int(r[1:]) >= 0):
                    obj.reg2 = get_index_of_register(r)
                elif r.find('(') != -1:
                    S = r.find('(')
                    T = r.find(')')
                    obj.reg2 = get_index_of_register(r[S + 1:T].strip())
                    obj.immediate = int(r[:S].strip())
                elif r[0] == '-' or r[0] == '0' or '0' <= r[0] <= '9':
                    if r[0] == '-':
                        if len(r) == 2:
                            obj.immediate = int(r)
                        elif r[1] == '0' and r[2] == 'x':
                            obj.immediate = int(r, 16)
                        elif r[1] == '0' and r[2] == 'b':
                            obj.immediate = int(r, 2)
                        else:
                            obj.immediate = int(r)
                    else:
                        if len(r) == 1:
                            obj.immediate = int(r)
                        elif r[0] == '0' and r[1] == 'x':
                            obj.immediate = int(r, 16)
                        elif r[0] == '0' and r[1] == 'b':
                            obj.immediate = int(r, 2)
                        else:
                            obj.immediate = int(r)
                else:
                    obj.jumptolabel = r

            elif count == 2:
                obj.reg1 = get_index_of_register(reg[:i1].strip())
                obj.reg2 = get_index_of_register(reg[i1 + 1:i2].strip())
                r = reg[i2 + 1:].strip()
                if len(r)>1 and (r == 'ra' or r == 'zero' or r == 'sp' or r == 'gp' or r == 'tp' or (
                        r[0] == 'x' and ord(r[1])>=ord('0') and ord(r[1])<=ord('9') and int(r[1:]) < 32 and int(r[1:]) >= 0) or (
                        r[0] == 't' and ord(r[1])>=ord('0') and ord(r[1])<=ord('9') and int(r[1:]) < 7 and int(r[1:]) >= 0) or (
                        r[0] == 's' and ord(r[1])>=ord('0') and ord(r[1])<=ord('9') and int(r[1:]) < 12 and int(r[1:]) >= 0) or (
                        r[0] == 'a' and ord(r[1])>=ord('0') and ord(r[1])<=ord('9') and int(r[1:]) < 8 and int(r[1:]) >= 0)):
                    obj.reg3 = get_index_of_register(r)
                elif r[0] == '-' or r[0] == '0' or '0' <= r[0] <= '9':
                    if r[0] == '-':
                        if len(r) == 2:
                            obj.immediate = int(r)
                        elif r[1] == '0' and r[2] == 'x':
                            obj.immediate = int(r, 16)
                        elif r[1] == '0' and r[2] == 'b':
                            obj.immediate = int(r, 2)
                        else:
                            obj.immediate = int(r)
                    else:
                        if len(r) == 1:
                            obj.immediate = int(r)
                        elif r[0] == '0' and r[1] == 'x':
                            obj.immediate = int(r, 16)
                        elif r[0] == '0' and r[1] == 'b':
                            obj.immediate = int(r, 2)
                        else:
                            obj.immediate = int(r)
                else:
                    obj.jumptolabel = r
            count = 0
            i1 = -1

            instruct_list.append(obj)

    file.close()
    # print(*instruct_list, sep="\n")

    # if __name__ == '__main__':
    #     print(*instruct_list, sep="\n")
    #     print()
    #     print(*data_list, sep="\n")

    # Instruct_nd_Variable_Names.printdicts()


    # print(Instruct_nd_Variable_Names.Instruct_names)
    return instruct_list,data_list





