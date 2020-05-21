import math
from register_file import *
import memory_normal
import PC
# import Instruct_nd_Variable_Names

# store_in_register(4,-1000)
# store_in_register(5,3)

def execute_R(op, rs1, rs2, rd):
    if op == 0:             # add
        w = load_from_register(rs1) + load_from_register(rs2)
        store_in_register(rd, w)
    elif op == 7:           # sub
        w=load_from_register(rs1) - load_from_register(rs2)
        store_in_register(rd, w)
    elif op == 9:           # mul
        w=load_from_register(rs1) * load_from_register(rs2)
        store_in_register(rd, w)
    elif op == 10:          # div
        w=int(load_from_register(rs1) / load_from_register(rs2))
        store_in_register(rd, w)
    elif op == 11:          # rem
        w=load_from_register(rs1) % load_from_register(rs2)
        store_in_register(rd, w)
    elif op == 1:           # and
        w=load_from_register(rs1) & load_from_register(rs2)
        store_in_register(rd, w)
    elif op == 2:       # or
        w=load_from_register(rs1) | load_from_register(rs2)
        store_in_register(rd, w)
    elif op == 8:       # xor
        w=load_from_register(rs1) ^ load_from_register(rs2)
        store_in_register(rd, w)
    elif op == 3:       # sll
        w=load_from_register(rs1) << load_from_register(rs2)
        store_in_register(rd, w)
    elif op == 5:       # sra
        w=load_from_register(rs1) >> load_from_register(rs2)
        store_in_register(rd, w)
    elif op == 4:       # slt
        if load_from_register(rs1) < load_from_register(rs2):  store_in_register(rd, 1)
        else:                   store_in_register(rd,0)
    elif op == 6:       # srl
        w=load_from_register(rs1) >> load_from_register(rs2) if load_from_register(rs1) >= 0 else (load_from_register(rs1) + 0x100000000) >> load_from_register(rs2)
        store_in_register(rd, w)

    PC.increment_PC()
# execute_R(6,4,5,6)
# print(load_from_register(6))
# print_all_registers()

def execute_I(op, rs1, rd, imm):
    if op == 12:        # addi
        w=load_from_register(rs1) + imm
        store_in_register(rd, w)
        PC.increment_PC()
    elif op == 13:     # andi
        w=load_from_register(rs1) & imm
        store_in_register(rd, w)
        PC.increment_PC()
    elif op == 14:     # ori
        w=load_from_register(rs1) | imm
        store_in_register(rd, w)
        PC.increment_PC()
    elif op == 15:       # lb
        w=memory_normal.read_byte_from_mem(load_from_register(rs1) + imm)
        store_in_register(rd, w)
        PC.increment_PC()
    elif op == 16:      # ld
        w=memory_normal.read_dword_from_mem(load_from_register(rs1) + imm)
        store_in_register(rd, w)
        PC.increment_PC()               # ld cant be supported ideally becoz reg is only 32 bit
    elif op == 17:       # lh
        w=memory_normal.read_hword_from_mem(load_from_register(rs1) + imm)
        store_in_register(rd, w)
        PC.increment_PC()
    elif op == 18:      # lw
        w=memory_normal.read_word_from_mem(load_from_register(rs1) + imm)
        store_in_register(rd, w)
        PC.increment_PC()
    elif op == 19:      # jalr
        store_in_register(rd, PC.PC +4)
        PC.PC = load_from_register(rs1) + imm

def execute_S(op, rs1, rs2, imm):
    if op == 23:        # sb
        memory_normal.write_byte_to_mem(load_from_register(rs1)+imm, load_from_register(rs2),1)
    elif op == 26:       # sh
        memory_normal.write_hword_to_mem(load_from_register(rs1) + imm, load_from_register(rs2))
    elif op == 24:      # sw
        memory_normal.write_word_to_mem(load_from_register(rs1) + imm, load_from_register(rs2))
    elif op == 25:      # sd
        memory_normal.write_dword_to_mem(load_from_register(rs1) + imm, load_from_register(rs2))
    PC.increment_PC()

def execute_UJ(op, rd, imm):
    if op == 20:        # jal
        if PC.PC + imm*2 >= memory_normal.code_stop:   PC.PC = memory_normal.code_stop
        else:
            store_in_register(rd, PC.PC + 4)
            PC.PC = PC.PC + imm * 2


def execute_U(op, rd, imm):
    if op == 21:        # lui
        store_in_register(rd, imm * int(math.pow(2,12)))
    elif op == 22:      # auipc
        store_in_register(rd, PC.PC + imm * int(math.pow(2,12)))
    PC.increment_PC()

def execute_SB(op, rs1, rs2, imm):
    if op == 27:  # beq
        if load_from_register(rs1) == load_from_register(rs2):
            PC.PC += imm * 2
        else:
            PC.increment_PC()
    elif op == 28:  # bne
        if load_from_register(rs1) != load_from_register(rs2):
            PC.PC += imm * 2
        else:
            PC.increment_PC()
    elif op == 29:  # bge
        if load_from_register(rs1) >= load_from_register(rs2):
            PC.PC += imm * 2
        else:
            PC.increment_PC()
    elif op == 30:  # blt
        if load_from_register(rs1) < load_from_register(rs2):
            PC.PC += imm * 2
        else:
            PC.increment_PC()
