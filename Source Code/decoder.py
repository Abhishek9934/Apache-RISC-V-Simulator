import memory
import EXEC_instruct
import PC
import register_file
import executed_information


def fetch(address):
    binary_equivalent = memory.read_code_line_from_mem(address)  # FETCH!!
    return binary_equivalent


def decode(binary_equivalent):        # DECODE 1 INSTRUCTION AT A TIME
    obj_op = -1
    obj_rs1= -1
    obj_rs2 = -1
    obj_rd = -1
    obj_imm = 0
    pass_value = -1
    d_stall = 0

    if binary_equivalent[25:] == '0110011':  # R-format
        if binary_equivalent[6] == '1':
            if binary_equivalent[17] == '0':
                obj_op = 9  # mul
            elif binary_equivalent[18] == '0':
                obj_op = 10  # div
            else:
                obj_op = 11  # rem
        elif binary_equivalent[1] == '1':
            if binary_equivalent[17] == '1':
                obj_op = 5  # sra
            else:
                obj_op = 7  # sub
        else:
            if binary_equivalent[17] == '0' and binary_equivalent[18] == '0' and binary_equivalent[
                19] == '0':     obj_op = 0
            if binary_equivalent[17] == '1' and binary_equivalent[18] == '1' and binary_equivalent[
                19] == '1':     obj_op = 1
            if binary_equivalent[17] == '1' and binary_equivalent[18] == '1' and binary_equivalent[
                19] == '0':     obj_op = 2
            if binary_equivalent[17] == '0' and binary_equivalent[18] == '0' and binary_equivalent[
                19] == '1':     obj_op = 3
            if binary_equivalent[17] == '0' and binary_equivalent[18] == '1' and binary_equivalent[
                19] == '0':     obj_op = 4
            if binary_equivalent[17] == '1' and binary_equivalent[18] == '0' and binary_equivalent[
                19] == '1':     obj_op = 6
            if binary_equivalent[17] == '1' and binary_equivalent[18] == '0' and binary_equivalent[
                19] == '0':     obj_op = 8
        obj_rs1 = int(binary_equivalent[12:17], 2)
        obj_rs2 = int(binary_equivalent[7:12], 2)
        obj_rd = int(binary_equivalent[20:25], 2)

    elif binary_equivalent[25:] == '1100111':  # jalr
        obj_op = 19
        if binary_equivalent[0]=='0':   obj_imm = int(binary_equivalent[1:12], 2)
        elif binary_equivalent[0]=='1':
            obj_imm = ((int(binary_equivalent[:12], 2)-1) ^ 0xfff) * -1
        obj_rs1 = int(binary_equivalent[12:17], 2)
        obj_rd = int(binary_equivalent[20:25], 2)
        pass_value = PC.PC + 4
        rs1_value = register_file.load_from_register(obj_rs1)
        if obj_rs1==executed_information.executed_info[-1][1] and (0<= executed_information.executed_info[-1][0] <=14 or executed_information.executed_info[-1][0]==22 or executed_information.executed_info[-1][0]==20):
            d_stall = 1
            return obj_op, obj_rd, obj_rs1, obj_rs2, obj_imm,pass_value,d_stall     ## 1 E-D stall
        if obj_rs1==executed_information.executed_info[-1][1] and 15 <= executed_information.executed_info[-1][0] <= 18:
            d_stall = 2                                                             ## 2 M-D stalls
            return obj_op, obj_rd, obj_rs1, obj_rs2, obj_imm,pass_value,d_stall
        if obj_rs1==executed_information.executed_info[-2][1] and 15 <= executed_information.executed_info[-2][0] <= 18:
            d_stall = 1                                                             ## 1 M-D stall
            return obj_op, obj_rd, obj_rs1, obj_rs2, obj_imm, pass_value, d_stall

        if (executed_information.executed_info[-1][1]==-3 or obj_rs1==executed_information.executed_info[-2][1]) and (0<= executed_information.executed_info[-2][0] <=14 or executed_information.executed_info[-2][0]==22 or executed_information.executed_info[-2][0]==20):
            rs1_value = executed_information.executed_info[-2][2]       ## E-D fwding
            executed_information.data_hazards += 1
        elif obj_rs1==executed_information.executed_info[-3][1] and (0<= executed_information.executed_info[-3][0] <=14 or executed_information.executed_info[-3][0]==22 or executed_information.executed_info[-3][0]==20):
            rs1_value = executed_information.executed_info[-3][2]       ## E-D fwding
            executed_information.data_hazards += 1

        if obj_rs1 == executed_information.executed_info[-3][1] and 15 <= executed_information.executed_info[-3][0] <=18 and (executed_information.executed_info[-1][1]>0 or 23<=executed_information.executed_info[-1][0]<=30 or executed_information.executed_info[-1][1]==-3) and (executed_information.executed_info[-2][1]>0 or 23<=executed_information.executed_info[-2][0]<=30 or executed_information.executed_info[-2][1]==-3):
            rs1_value = executed_information.executed_info[-2][6]       ## M-D fwding
            executed_information.data_hazards += 1

        cf1 = PC.PC
        if cf1 not in executed_information.branch_child.keys():
            cf2 = rs1_value + obj_imm
            executed_information.add_to_branch_child(cf1, cf2)
            executed_information.add_to_branch_taken(cf1, 1)

        PC.PC = rs1_value + obj_imm


    elif binary_equivalent[25:] == '0010011':  # addi,andi,ori
        if binary_equivalent[19] == '1':
            obj_op = 13  # andi
        elif binary_equivalent[17] == '1':
            obj_op = 14  # ori
        else:
            obj_op = 12  # addi
        if binary_equivalent[0]=='0':   obj_imm = int(binary_equivalent[1:12], 2)
        elif binary_equivalent[0]=='1':
            obj_imm = ((int(binary_equivalent[:12], 2)-1) ^ 0xfff) * -1
        obj_rs1 = int(binary_equivalent[12:17], 2)
        obj_rd = int(binary_equivalent[20:25], 2)

    elif binary_equivalent[25:] == '0000011':
        if binary_equivalent[17:20] == '000':
            obj_op = 15  # lb
        elif binary_equivalent[17:20] == '011':
            obj_op = 16  # ld
        elif binary_equivalent[17:20] == '001':
            obj_op = 17  # lh
        elif binary_equivalent[17:20] == '010':
            obj_op = 18  # lw
        if binary_equivalent[0]=='0':   obj_imm = int(binary_equivalent[1:12], 2)
        elif binary_equivalent[0]=='1':
            obj_imm = ((int(binary_equivalent[:12], 2)-1) ^ 0xfff) * -1
        obj_rs1 = int(binary_equivalent[12:17], 2)
        obj_rd = int(binary_equivalent[20:25], 2)

    elif binary_equivalent[25:] == '1101111':  # jal
        obj_op = 20
        obj_rd = int(binary_equivalent[20:25], 2)
        CIS = int(
            binary_equivalent[0] + binary_equivalent[12:20] + binary_equivalent[11] + binary_equivalent[1:11], 2)
        if binary_equivalent[0] == '0': obj_imm = CIS
        elif binary_equivalent[0] == '1':   obj_imm = ((CIS-1)^0xfffff)*-1

        cf1 = PC.PC
        if cf1 not in executed_information.branch_child.keys():
            cf2 = cf1 + obj_imm*2
            executed_information.add_to_branch_child(cf1,cf2)
            executed_information.add_to_branch_taken(cf1,1)

        if PC.PC + obj_imm * 2 >= memory.code_stop:
            PC.PC = memory.code_stop
        else:
            pass_value = PC.PC + 4
            PC.PC += obj_imm * 2


    elif binary_equivalent[25:] == '0110111':  # lui
        obj_op = 21
        obj_rd = int(binary_equivalent[20:25], 2)
        obj_imm = int(binary_equivalent[0:20], 2)

    elif binary_equivalent[25:] == '0010111':  # auipc
        obj_op = 22
        obj_rd = int(binary_equivalent[20:25], 2)
        obj_imm = int(binary_equivalent[0:20], 2)

    elif binary_equivalent[25:] == '0100011':  # S-format
        if binary_equivalent[18:20] == '00':
            obj_op = 23  # sb
        elif binary_equivalent[18:20] == '10':
            obj_op = 24  # sw
        elif binary_equivalent[18:20] == '11':
            obj_op = 25  # sd
        elif binary_equivalent[18:20] == '01':
            obj_op = 26  # sh
        obj_rs2 = int(binary_equivalent[7:12], 2)
        obj_rs1 = int(binary_equivalent[12:17], 2)
        CIS = int(binary_equivalent[0:7] + binary_equivalent[20:25], 2)
        if binary_equivalent[0] == '0': obj_imm = CIS
        elif binary_equivalent[0] == '1':   obj_imm = ((CIS-1)^0xfff) * -1

    elif binary_equivalent[25:] == '1100011':  # SB-format
        CIS = int(
            binary_equivalent[0] + binary_equivalent[24] + binary_equivalent[1:7] + binary_equivalent[20:24], 2)
        if binary_equivalent[0] == '0':
            obj_imm = CIS
        elif binary_equivalent[0] == '1':
            obj_imm = ((CIS - 1) ^ 0xfff) * -1
        obj_rs2 = int(binary_equivalent[7:12], 2)
        obj_rs1 = int(binary_equivalent[12:17], 2)

        rs1_value = register_file.load_from_register(obj_rs1)
        rs2_value = register_file.load_from_register(obj_rs2)

        if binary_equivalent[17] == '0' and binary_equivalent[19] == '0':       obj_op = 27  # beq
        elif binary_equivalent[17] == '0' and binary_equivalent[19] == '1':     obj_op = 28  # bne
        elif binary_equivalent[17] == '1' and binary_equivalent[19] == '1':     obj_op = 29  # bge
        elif binary_equivalent[17] == '1' and binary_equivalent[19] == '0':     obj_op = 30  # blt

        if (obj_rs1 == executed_information.executed_info[-1][1] or obj_rs2 == executed_information.executed_info[-1][1]) and (0 <= executed_information.executed_info[-1][0] <= 14 or 19 <= executed_information.executed_info[-1][0] <= 22):
            d_stall = 1
            return obj_op, obj_rd, obj_rs1, obj_rs2, obj_imm, pass_value, d_stall       ## 1 E-D stall
        if (obj_rs1 == executed_information.executed_info[-1][1] or obj_rs2 == executed_information.executed_info[-1][1]) and 15<=executed_information.executed_info[-1][0]<=18:
            d_stall = 2
            return obj_op, obj_rd, obj_rs1, obj_rs2, obj_imm, pass_value, d_stall       ## 2 M-D stalls
        if (obj_rs1 == executed_information.executed_info[-2][1] or obj_rs2 == executed_information.executed_info[-2][1]) and 15<=executed_information.executed_info[-2][0]<=18:
            d_stall = 1
            return obj_op, obj_rd, obj_rs1, obj_rs2, obj_imm, pass_value, d_stall       ## 1 M-D stall


        if executed_information.executed_info[-1][1] == -3 and (0 <= executed_information.executed_info[-2][0] <= 14 or 19 <= executed_information.executed_info[-2][0] <= 22):
            if obj_rs1 == executed_information.executed_info[-2][1]:
                rs1_value = executed_information.executed_info[-2][2]                   ## E-D fwding
                executed_information.data_hazards += 1
            if obj_rs2 == executed_information.executed_info[-2][1]:
                rs2_value = executed_information.executed_info[-2][2]                   ## E-D fwding
                executed_information.data_hazards += 1
        else:
            if (obj_rs1 == executed_information.executed_info[-2][1]) and (0 <= executed_information.executed_info[-2][0] <= 14 or 19 <= executed_information.executed_info[-2][0] <= 22):
                rs1_value = executed_information.executed_info[-2][2]                   ## E-D fwding
                executed_information.data_hazards += 1
            elif (obj_rs1 == executed_information.executed_info[-3][1]) and (0 <= executed_information.executed_info[-3][0] <= 14 or 19 <= executed_information.executed_info[-3][0] <= 22):
                rs1_value = executed_information.executed_info[-3][2]                   ## E-D fwding
                executed_information.data_hazards += 1

            if (obj_rs2 == executed_information.executed_info[-2][1]) and (0 <= executed_information.executed_info[-2][0] <= 14 or 19 <= executed_information.executed_info[-2][0] <= 22):
                rs2_value = executed_information.executed_info[-2][2]                   ## E-D fwding
                executed_information.data_hazards += 1
            elif (obj_rs2 == executed_information.executed_info[-3][1]) and (0 <= executed_information.executed_info[-3][0] <= 14 or 19 <= executed_information.executed_info[-3][0] <= 22):
                rs2_value = executed_information.executed_info[-3][2]                   ## E-D fwding
                executed_information.data_hazards += 1

        if obj_rs1 == executed_information.executed_info[-3][1] and 15<=executed_information.executed_info[-3][0] <=18 and (executed_information.executed_info[-1][1]>0 or 23<=executed_information.executed_info[-1][0]<=30 or executed_information.executed_info[-1][1]==-3) and (executed_information.executed_info[-2][1]>0 or 23<=executed_information.executed_info[-2][0]<=30 or executed_information.executed_info[-2][1]==-3):
            rs1_value = executed_information.executed_info[-2][6]                       # M-D fwding
            executed_information.data_hazards += 1
        if obj_rs2 == executed_information.executed_info[-3][1] and 15<=executed_information.executed_info[-3][0] <=18 and (executed_information.executed_info[-1][1]>0 or 23<=executed_information.executed_info[-1][0]<=30 or executed_information.executed_info[-1][1]==-3) and (executed_information.executed_info[-2][1]>0 or 23<=executed_information.executed_info[-2][0]<=30 or executed_information.executed_info[-2][1]==-3):
            rs2_value = executed_information.executed_info[-2][6]                       # M-D fwding
            executed_information.data_hazards += 1

        cf1 = PC.PC
        if cf1 not in executed_information.branch_child.keys():
            cf2 = cf1 + obj_imm*2
            executed_information.add_to_branch_child(cf1,cf2)

        if binary_equivalent[17] == '0' and binary_equivalent[19] == '0':
            obj_op = 27  # beq
            if rs1_value == rs2_value:
                PC.PC += obj_imm * 2
                executed_information.add_to_branch_taken(cf1,1)
            else:
                PC.increment_PC()
                executed_information.add_to_branch_taken(cf1, 0)
        elif binary_equivalent[17] == '0' and binary_equivalent[19] == '1':
            obj_op = 28  # bne
            if rs1_value != rs2_value:
                PC.PC += obj_imm * 2
                executed_information.add_to_branch_taken(cf1, 1)
            else:
                PC.increment_PC()
                executed_information.add_to_branch_taken(cf1, 0)
        elif binary_equivalent[17] == '1' and binary_equivalent[19] == '1':
            obj_op = 29  # bge
            if rs1_value >= rs2_value:
                PC.PC += obj_imm * 2
                executed_information.add_to_branch_taken(cf1, 1)
            else:
                PC.increment_PC()
                executed_information.add_to_branch_taken(cf1, 0)
        elif binary_equivalent[17] == '1' and binary_equivalent[19] == '0':
            obj_op = 30  # blt
            if rs1_value < rs2_value:
                PC.PC += obj_imm * 2
                executed_information.add_to_branch_taken(cf1, 1)
            else:
                PC.increment_PC()
                executed_information.add_to_branch_taken(cf1, 0)

    # decoded_result = (op,rd,rs1,rs2,imm,pass_value)
    return obj_op, obj_rd, obj_rs1, obj_rs2, obj_imm,pass_value,d_stall




