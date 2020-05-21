from dataclasses import dataclass
import memory_normal
import EXEC_instruct_normal

@dataclass
class instruction():
    address: str = None
    operation: int = -1
    rs1: int = -1
    rs2: int = -1
    rd: int = -1
    immediate: int = 0

def decode(address):        # PROCESS 1 INSTRUCTION AT A TIME
    obj = instruction()
    binary_equivalent = memory_normal.read_code_line_from_mem(address)     # FETCH!!
    # DECODE!!
    if binary_equivalent[25:] == '0110011':  # R-format
        if binary_equivalent[6] == '1':
            if binary_equivalent[17] == '0':
                obj.operation = 9  # mul
            elif binary_equivalent[18] == '0':
                obj.operation = 10  # div
            else:
                obj.operation = 11  # rem
        elif binary_equivalent[1] == '1':
            if binary_equivalent[17] == '1':
                obj.operation = 5  # sra
            else:
                obj.operation = 7  # sub
        else:
            if binary_equivalent[17] == '0' and binary_equivalent[18] == '0' and binary_equivalent[
                19] == '0':     obj.operation = 0
            if binary_equivalent[17] == '1' and binary_equivalent[18] == '1' and binary_equivalent[
                19] == '1':     obj.operation = 1
            if binary_equivalent[17] == '1' and binary_equivalent[18] == '1' and binary_equivalent[
                19] == '0':     obj.operation = 2
            if binary_equivalent[17] == '0' and binary_equivalent[18] == '0' and binary_equivalent[
                19] == '1':     obj.operation = 3
            if binary_equivalent[17] == '0' and binary_equivalent[18] == '1' and binary_equivalent[
                19] == '0':     obj.operation = 4
            if binary_equivalent[17] == '1' and binary_equivalent[18] == '0' and binary_equivalent[
                19] == '1':     obj.operation = 6
            if binary_equivalent[17] == '1' and binary_equivalent[18] == '0' and binary_equivalent[
                19] == '0':     obj.operation = 8
        obj.rs1 = int(binary_equivalent[12:17], 2)
        obj.rs2 = int(binary_equivalent[7:12], 2)
        obj.rd = int(binary_equivalent[20:25], 2)
        EXEC_instruct_normal.execute_R(obj.operation, obj.rs1, obj.rs2, obj.rd)        # EXECUTE!!

    elif binary_equivalent[25:] == '1100111':  # jalr
        obj.operation = 19
        if binary_equivalent[0]=='0':   obj.immediate = int(binary_equivalent[1:12], 2)
        elif binary_equivalent[0]=='1':
            obj.immediate = ((int(binary_equivalent[:12], 2)-1) ^ 0xfff) * -1
        obj.rs1 = int(binary_equivalent[12:17], 2)
        obj.rd = int(binary_equivalent[20:25], 2)
        EXEC_instruct_normal.execute_I(obj.operation, obj.rs1, obj.rd, obj.immediate)  # EXECUTE!!
    elif binary_equivalent[25:] == '0010011':  # addi,andi,ori
        # print("Fuck")
        if binary_equivalent[19] == '1':
            obj.operation = 13  # andi
        elif binary_equivalent[17] == '1':
            obj.operation = 14  # ori
        else:
            obj.operation = 12  # addi
        if binary_equivalent[0]=='0':   obj.immediate = int(binary_equivalent[1:12], 2)
        elif binary_equivalent[0]=='1':
            obj.immediate = ((int(binary_equivalent[:12], 2)-1) ^ 0xfff) * -1
        obj.rs1 = int(binary_equivalent[12:17], 2)
        obj.rd = int(binary_equivalent[20:25], 2)
        EXEC_instruct_normal.execute_I(obj.operation, obj.rs1, obj.rd, obj.immediate)  # EXECUTE!!
    elif binary_equivalent[25:] == '0000011':
        if binary_equivalent[17:20] == '000':
            obj.operation = 15  # lb
        elif binary_equivalent[17:20] == '011':
            obj.operation = 16  # ld
        elif binary_equivalent[17:20] == '001':
            obj.operation = 17  # lh
        elif binary_equivalent[17:20] == '010':
            obj.operation = 18  # lw
        if binary_equivalent[0]=='0':   obj.immediate = int(binary_equivalent[1:12], 2)
        elif binary_equivalent[0]=='1':
            obj.immediate = ((int(binary_equivalent[:12], 2)-1) ^ 0xfff) * -1
        obj.rs1 = int(binary_equivalent[12:17], 2)
        obj.rd = int(binary_equivalent[20:25], 2)
        EXEC_instruct_normal.execute_I(obj.operation, obj.rs1, obj.rd, obj.immediate)  # EXECUTE!!
    elif binary_equivalent[25:] == '1101111':  # jal
        obj.operation = 20
        obj.rd = int(binary_equivalent[20:25], 2)
        CIS = int(
            binary_equivalent[0] + binary_equivalent[12:20] + binary_equivalent[11] + binary_equivalent[1:11], 2)
        if binary_equivalent[0] == '0': obj.immediate = CIS
        elif binary_equivalent[0] == '1':   obj.immediate = ((CIS-1)^0xfffff)*-1
        EXEC_instruct_normal.execute_UJ(obj.operation, obj.rd, obj.immediate)  # EXECUTE!!
    elif binary_equivalent[25:] == '0110111':  # lui
        obj.operation = 21
        obj.rd = int(binary_equivalent[20:25], 2)
        obj.immediate = int(binary_equivalent[0:20], 2)
        EXEC_instruct_normal.execute_U(obj.operation, obj.rd, obj.immediate)   # EXECUTE!!
    elif binary_equivalent[25:] == '0010111':  # auipc
        obj.operation = 22
        obj.rd = int(binary_equivalent[20:25], 2)
        obj.immediate = int(binary_equivalent[0:20], 2)
        EXEC_instruct_normal.execute_U(obj.operation, obj.rd, obj.immediate)   # EXECUTE!!
    elif binary_equivalent[25:] == '0100011':  # S-format
        if binary_equivalent[18:20] == '00':
            obj.operation = 23  # sb
        elif binary_equivalent[18:20] == '10':
            obj.operation = 24  # sw
        elif binary_equivalent[18:20] == '11':
            obj.operation = 25  # sd
        elif binary_equivalent[18:20] == '01':
            obj.operation = 26  # sh
        obj.rs2 = int(binary_equivalent[7:12], 2)
        obj.rs1 = int(binary_equivalent[12:17], 2)
        CIS = int(binary_equivalent[0:7] + binary_equivalent[20:25], 2)
        if binary_equivalent[0] == '0': obj.immediate = CIS
        elif binary_equivalent[0] == '1':   obj.immediate = ((CIS-1)^0xfff) * -1
        EXEC_instruct_normal.execute_S(obj.operation, obj.rs1, obj.rs2, obj.immediate)     # EXECUTE!!
    elif binary_equivalent[25:] == '1100011':  # SB-format
        if binary_equivalent[17] == '0' and binary_equivalent[19] == '0':
            obj.operation = 27  # beq
        elif binary_equivalent[17] == '0' and binary_equivalent[19] == '1':
            obj.operation = 28  # bne
        elif binary_equivalent[17] == '1' and binary_equivalent[19] == '1':
            obj.operation = 29  # bge
        elif binary_equivalent[17] == '1' and binary_equivalent[19] == '0':
            obj.operation = 30  # blt
        CIS = int(
            binary_equivalent[0] + binary_equivalent[24] + binary_equivalent[1:7] + binary_equivalent[20:24], 2)
        if binary_equivalent[0] == '0': obj.immediate = CIS
        elif binary_equivalent[0] == '1':   obj.immediate = ((CIS-1)^0xfff) * -1
        obj.rs2 = int(binary_equivalent[7:12], 2)
        obj.rs1 = int(binary_equivalent[12:17], 2)
        EXEC_instruct_normal.execute_SB(obj.operation, obj.rs1, obj.rs2, obj.immediate)    # EXECUTE!!





