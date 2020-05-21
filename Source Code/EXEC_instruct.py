import math
from register_file import *
import memory
import PC
import executed_information
# import Instruct_nd_Variable_Names


def execute_instruction(decoded_result):
    op = decoded_result[0]
    rd = decoded_result[1]
    rs1 = decoded_result[2]
    rs2 = decoded_result[3]
    imm = decoded_result[4]
    pass_value = decoded_result[5]

    m_read = -1
    r_index = -1
    r_value = 0
    m_index = -1
    m_value = 0
    m_type = -1
    stall_flag = 0

    if (0 <= op <= 14 or op == 19) and 15<= executed_information.executed_info[-1][0] <=18 and (rs1==executed_information.executed_info[-1][1] or rs2==executed_information.executed_info[-1][1]):
        stall_flag=1
        return -op-1, r_index, r_value, m_index, m_value, m_type, m_read, stall_flag      # -op-1 means special case of R follows L

    if rs1 and executed_information.executed_info[-1][1] == rs1:
        rs1_value = executed_information.executed_info[-1][2]
        executed_information.data_hazards += 1
    elif rs1 and executed_information.executed_info[-2][1] == rs1:
        rs1_value = executed_information.executed_info[-2][2]
        executed_information.data_hazards += 1
    else:                         rs1_value = load_from_register(rs1)     # E-E fwding

    if rs2 and executed_information.executed_info[-1][1] == rs2:
        rs2_value = executed_information.executed_info[-1][2]
        executed_information.data_hazards += 1
    elif rs2 and executed_information.executed_info[-2][1] == rs2:
        rs2_value = executed_information.executed_info[-2][2]
        executed_information.data_hazards += 1
    else:                         rs2_value = load_from_register(rs2)     # E-E fwding

    if executed_information.executed_info[-1][0] < 0:       # M-E fwding  (R follows L)
        if rs1>=0 and rs1==executed_information.executed_info[-2][1]:
            rs1_value = executed_information.executed_info[-1][6]
            executed_information.data_hazards += 1
        elif rs2>=0 and rs2==executed_information.executed_info[-2][1]:
            rs2_value = executed_information.executed_info[-1][6]
            executed_information.data_hazards += 1

    if (0 <= op <= 14 or op == 19) and 15<= executed_information.executed_info[-2][0] <=18 and (rs1==executed_information.executed_info[-2][1] or rs2==executed_information.executed_info[-2][1]):   # M-E fwding
        if rs1>=0 and rs1==executed_information.executed_info[-2][1]:
            rs1_value = executed_information.executed_info[-1][6]
            executed_information.data_hazards += 1
        elif rs2>=0 and rs2==executed_information.executed_info[-2][1]:
            rs2_value = executed_information.executed_info[-1][6]
            executed_information.data_hazards += 1


    if op == 0:  # add
        w = rs1_value + rs2_value
        r_index = rd
        r_value = w
        PC.increment_PC()
    elif op == 7:  # sub
        w = rs1_value - rs2_value
        r_index = rd
        r_value = w
        PC.increment_PC()
    elif op == 9:  # mul
        w = rs1_value * rs2_value
        r_index = rd
        r_value = w
        PC.increment_PC()
    elif op == 10:  # div
        w = int(rs1_value / rs2_value)
        r_index = rd
        r_value = w
        PC.increment_PC()
    elif op == 11:  # rem
        w = rs1_value % rs2_value
        r_index = rd
        r_value = w
        PC.increment_PC()
    elif op == 1:  # and
        w = rs1_value & rs2_value
        r_index = rd
        r_value = w
        PC.increment_PC()
    elif op == 2:  # or
        w = rs1_value | rs2_value
        r_index = rd
        r_value = w
        PC.increment_PC()
    elif op == 8:  # xor
        w = rs1_value ^ rs2_value
        r_index = rd
        r_value = w
        PC.increment_PC()
    elif op == 3:  # sll
        w = rs1_value << rs2_value
        r_index = rd
        r_value = w
        PC.increment_PC()
    elif op == 5:  # sra
        w = rs1_value >> rs2_value
        r_index = rd
        r_value = w
        PC.increment_PC()
    elif op == 4:  # slt
        if rs1_value < rs2_value:
            r_index = rd
            r_value = 1
        else:
            r_index = rd
            r_value = 0
        PC.increment_PC()
    elif op == 6:  # srl
        w = rs1_value >> rs2_value if rs1_value >= 0 else (rs1_value + 0x100000000) >> rs2_value
        r_index = rd
        r_value = w
        PC.increment_PC()

    elif op == 12:  # addi
        w = rs1_value + imm
        r_index = rd
        r_value = w
        PC.increment_PC()
    elif op == 13:  # andi
        w = rs1_value & imm
        r_index = rd
        r_value = w
        PC.increment_PC()
    elif op == 14:  # ori
        w = rs1_value | imm
        r_index = rd
        r_value = w
        PC.increment_PC()
    elif op == 15:  # lb
        m_index = rs1_value + imm
        r_index = rd
        #r_value = w
        m_type = 0
        m_read = 1
        PC.increment_PC()
        executed_information.data_transfer_instructs+=1
    elif op == 16:  # ld
        m_index = rs1_value + imm
        r_index = rd
        #r_value = w
        m_type = 3
        m_read = 1
        PC.increment_PC()       # ld cant be supported ideally becoz reg is only 32 bit
        executed_information.data_transfer_instructs += 1
    elif op == 17:  # lh
        m_index = rs1_value + imm
        r_index = rd
        # r_value = w
        m_type = 1
        m_read = 1
        PC.increment_PC()
        executed_information.data_transfer_instructs += 1
    elif op == 18:  # lw
        m_index = rs1_value + imm
        r_index = rd
        # r_value = w
        m_type = 2
        m_read = 1
        PC.increment_PC()
        executed_information.data_transfer_instructs += 1
    elif op == 19:  # jalr
        r_index = rd
        r_value = pass_value

    elif op == 23:  # sb
        m_index = rs1_value + imm
        m_value = rs2_value
        m_type = 0
        m_read = 0
        r_index = -rs2
        PC.increment_PC()
        executed_information.data_transfer_instructs += 1
    elif op == 26:  # sh
        m_index = rs1_value + imm
        m_value = rs2_value
        m_type = 1
        m_read = 0
        r_index = -rs2
        PC.increment_PC()
        executed_information.data_transfer_instructs += 1
    elif op == 24:  # sw
        m_index = rs1_value + imm
        m_value = rs2_value
        m_type = 2
        m_read = 0
        r_index = -rs2
        PC.increment_PC()
        executed_information.data_transfer_instructs += 1
    elif op == 25:  # sd
        m_index = rs1_value + imm
        m_value = rs2_value
        m_type =3
        m_read = 0
        r_index = -rs2
        PC.increment_PC()
        executed_information.data_transfer_instructs += 1

    elif op == 20:  # jal
        if PC.PC < memory.code_stop:
            r_value = pass_value
            r_index = rd

    elif op == 21:  # lui
        r_index = rd
        r_value = imm * int(math.pow(2, 12))
        PC.increment_PC()

    elif op == 22:  # auipc
        r_index = rd
        r_value = PC.PC + imm * int(math.pow(2, 12))
        PC.increment_PC()

    # elif op == 27:  # beq
    #     if rs1_value == rs2_value:
    #         PC.PC += imm * 2
    #     else:
    #         PC.increment_PC()
    # elif op == 28:  # bne
    #     if rs1_value != rs2_value:
    #         PC.PC += imm * 2
    #     else:
    #         PC.increment_PC()
    # elif op == 29:  # bge
    #     if rs1_value >= rs2_value:
    #         PC.PC += imm * 2
    #     else:
    #         PC.increment_PC()
    # elif op == 30:  # blt
    #     if rs1_value < rs2_value:
    #         PC.PC += imm * 2
    #     else:
    #         PC.increment_PC()

    if 0<=op<=14 or 21<=op<=22:
        executed_information.alu_instructs += 1
    if 27<=op<=30 or 19<=op<=20:
        executed_information.control_instructs += 1

    return op,r_index,r_value,m_index,m_value,m_type,m_read,stall_flag


def write_back(r_index,r_value):
    if r_index > 0:     store_in_register(r_index,r_value)
