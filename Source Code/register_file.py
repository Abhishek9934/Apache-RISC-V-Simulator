import math
reg_address_to_value={}                    # a dictionary
for i in range(32):
    if i == 2:  reg_address_to_value[i]  = 0x7ffffff0
    elif i == 3:    reg_address_to_value[i] = 0x10000000
    else:   reg_address_to_value[i] = 0       # register can store a number only. It can never store a string.

def store_in_register(index,value):     # index can only be from 0 to 31
    if index == 0:   return
    elif index < 0 or index > 31: return
    elif (value >= 0 and value < math.pow(2,32)) or (value < 0 and (value*-1) < math.pow(2,31)):
        reg_address_to_value[index] = value
    else: print(f"Value overflow in register {index}")

def load_from_register(index):
    if index <= 0 or index > 31:    return 0
    return reg_address_to_value[index]

def print_all_registers():
    for i in range(32):
        print(f"x{i} = {hex(reg_address_to_value[i])}")

def print_selected_registers():
    for i in range(32):
        if reg_address_to_value[i]:    print(f"x{i} = {hex(reg_address_to_value[i])}")

def print_register(index):
    print(f'x{index} = {reg_address_to_value[index]}')



